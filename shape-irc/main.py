#!/usr/bin/env python3
"""
An IRC bot that connects to an IRC server, joins a channel, and responds to messages using the Shapes LLM API.
"""

import irc.bot
import irc.strings
import ssl
import time
import irc.connection
import os
import sys
import asyncio
import argparse
import aiohttp
from dotenv import load_dotenv
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion

# Load environment variables from .env file
load_dotenv()

class IRCBot(irc.bot.SingleServerIRCBot):
    def __init__(self, nickname, server, channel, port=6697, dev_mode=False):
        # Initialize OpenAI client for Shapes API
        self.shape_api_key = os.getenv("SHAPESINC_API_KEY")
        self.shape_username = os.getenv("SHAPESINC_SHAPE_USERNAME")
        self.dev_mode = dev_mode
        
        if not self.shape_api_key:
            print("Warning: SHAPESINC_API_KEY not found in .env")
        
        if not self.shape_username:
            print("Warning: SHAPESINC_SHAPE_USERNAME not found in .env")
        
        # Use localhost:8080 in dev mode, otherwise use the Shapes API
        if self.dev_mode:
            self.api_base_url = "http://localhost:8080/v1"
            print(f"DEV MODE: Using local server at {self.api_base_url}")
        else:
            self.api_base_url = "https://api.shapes.inc/v1"
            
        self.aclient_shape = AsyncOpenAI(
            api_key=self.shape_api_key,
            base_url=self.api_base_url,
        )
        # Create SSL wrapper for the socket
        ssl_context = ssl.create_default_context()
        factory = irc.connection.Factory(wrapper=lambda sock: ssl_context.wrap_socket(sock, server_hostname=server))
        
        # Initialize the bot
        irc.bot.SingleServerIRCBot.__init__(
            self, 
            [(server, port)], 
            nickname, 
            nickname,
            connect_factory=factory
        )
        
        self.channel = channel
        
    def on_welcome(self, connection, event):
        """Called when the bot successfully connects to the server."""
        print(f"Connected to {connection.get_server_name()}")
        connection.join(self.channel)
        
    def on_join(self, connection, event):
        """Called when the bot joins a channel."""
        # Check if it's our bot that joined
        if event.source.nick == connection.get_nickname():
            print(f"Joined {event.target}")
            
    def on_pubmsg(self, connection, event):
        """Called when a message is received in a channel."""
        message = event.arguments[0]
        sender = event.source.nick
        
        # Don't respond to our own messages
        if sender == connection.get_nickname():
            return
            
        print(f"Message from {sender}: {message}")
        
        # Check if the message is the !wack command
        if message.strip() == "!wack":
            response = asyncio.run(self.handle_wack_command())
        else:
            # Generate a response using the LLM
            response = asyncio.run(self.generate_llm_response(sender, message))
        
        if response:
            # Clean the response by replacing newlines and carriage returns with spaces
            clean_response = response.replace('\n', ' ').replace('\r', ' ')
            print(f"Sending to IRC: {clean_response}")
            # Send the response to the channel
            connection.privmsg(self.channel, clean_response)
            
    async def handle_wack_command(self):
        """Handle the !wack command by hitting the /wack endpoint."""
        try:
            if not self.shape_api_key or not self.shape_username:
                print("Not configured to handle wack command")
                return None
                
            # Construct the full URL with the model parameter using the global base_url
            url = f"{self.api_base_url}/wack?model=shapesinc/{self.shape_username}"
            
            print(f"Sending request to: {url}")
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers={
                    "Authorization": f"Bearer {self.shape_api_key}",
                    "X-Channel-Id": self.channel
                }) as response:
                    if response.status == 200:
                        result = await response.text()
                        print(f"Wack response: {result}")
                        return "*ouch*"
                    else:
                        error_text = await response.text()
                        print(f"Error from wack endpoint: {response.status} - {error_text}")
                        return None
                        
        except Exception as e:
            print(f"Error handling wack command: {e}")
            return None
            
    async def generate_llm_response(self, sender, message):
        """Generate a response using the Shapes LLM API."""
        try:
            if not self.shape_api_key or not self.shape_username:
                return "Sorry, I'm not configured to generate responses yet."
                
            messages = [
                {
                    "role": "user",
                    "content": message,
                }
            ]
            
            # Send the message to the shape
            print(f"Sending to Shapes API: {messages}")
            resp = await self.aclient_shape.chat.completions.create(
                model=f"shapesinc/{self.shape_username}",
                messages=messages,
                extra_headers={
                    "X-User-Id": sender,  # Use the IRC nickname as the user ID
                    "X-Channel-Id": self.channel,  # Use the IRC channel name
                },
            )
            
            print(f"Raw API response: {resp}")
            
            if resp.choices and len(resp.choices) > 0:
                response_content = resp.choices[0].message.content
                print(f"Response content: {response_content}")
                return response_content
            else:
                print("No choices in response")
                return "Sorry, I couldn't generate a response."
                
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Sorry, I encountered an error while generating a response."

async def get_shape_name(api_key, dev_mode=False):
    """Fetch the shape name from the API."""
    try:
        # Determine base URL based on dev mode
        if dev_mode:
            base_url = "http://localhost:8080/v1"
        else:
            base_url = "https://api.shapes.inc/v1"
            
        url = f"{base_url}/shape_name"
        
        print(f"Fetching shape name from: {url}")
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers={"Authorization": f"Bearer {api_key}"}) as response:
                if response.status == 200:
                    result = await response.json()
                    shape_name = result.get("name")
                    print(f"Shape name: {shape_name}")
                    return shape_name
                else:
                    error_text = await response.text()
                    print(f"Error fetching shape name: {response.status} - {error_text}")
                    return None
                    
    except Exception as e:
        print(f"Error fetching shape name: {e}")
        return None

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='IRC bot that uses Shapes LLM API')
    parser.add_argument('--channel', required=True, help='IRC channel to join (without # prefix)')
    parser.add_argument('--server', required=True, help='IRC server to connect to')
    parser.add_argument('--shape', help='Shape name to use (will be used as nickname)')
    parser.add_argument('--port', type=int, default=6697, help='IRC server port (default: 6697 for SSL)')
    parser.add_argument('--dev', action='store_true', help='Use local development server at localhost:8080')
    
    args = parser.parse_args()
    
    # Add the # prefix if not provided
    channel = args.channel
    if not channel.startswith("#"):
        channel = f"#{channel}"
    
    # Check if dev mode is enabled
    dev_mode = args.dev
    
    # Get the API key from environment
    api_key = os.getenv("SHAPESINC_API_KEY")
    if not api_key:
        print("Error: SHAPESINC_API_KEY not found in environment")
        sys.exit(1)
    
    # Get the shape name (nickname)
    if args.shape:
        nickname = args.shape
    else:
        # Fetch the shape name from the API
        print("No shape name provided, fetching from API...")
        nickname = asyncio.run(get_shape_name(api_key, dev_mode))
        if not nickname:
            print("Error: Could not fetch shape name from API")
            sys.exit(1)
        print(f"Using shape name: {nickname}")
    
    server = args.server
    port = args.port
    
    bot = IRCBot(nickname, server, channel, port, dev_mode=dev_mode)
    try:
        print(f"Connecting to {server}:{port} as {nickname}...")
        bot.start()
    except KeyboardInterrupt:
        print("Bot shutting down...")
        bot.disconnect()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
