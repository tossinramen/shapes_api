const axios = require('axios');
require('dotenv').config();

// Configuration
const REVOLT_TOKEN = process.env.REVOLT_TOKEN;
const SHAPES_API_KEY = process.env.SHAPESINC_API_KEY;
const SHAPES_USERNAME = process.env.SHAPESINC_SHAPE_USERNAME;
const SHAPES_API_URL = 'https://api.shapes.inc/v1/chat/completions';
const REVOLT_API_URL = 'https://api.revolt.chat';

// Bot information
let botId = null;
let botUsername = null;

// Create websocket connection to Revolt
const WebSocket = require('ws');
const EventEmitter = require('events');
const events = new EventEmitter();

async function startBot() {
  try {
    // Get bot info first
    const { data: self } = await axios.get(`${REVOLT_API_URL}/users/@me`, {
      headers: { 'x-bot-token': REVOLT_TOKEN }
    });
    
    botId = self._id;
    botUsername = self.username;
    console.log(`Logged in as ${botUsername} (${botId})`);
    
    // Connect using the correct WebSocket URL for bots
    const socket = new WebSocket('wss://ws.revolt.chat');
    
    socket.on('open', () => {
      console.log('Connected to Revolt WebSocket');
      // Authenticate with bot token
      socket.send(JSON.stringify({
        type: 'Authenticate',
        token: REVOLT_TOKEN
      }));
    });
    
    socket.on('message', async (data) => {
      try {
        const message = JSON.parse(data);
        console.log('Received message:', message.type);
        
        if (message.type === 'Ready') {
          console.log('Bot is ready to receive messages');
        }
        
        if (message.type === 'Message') {
          // Ignore our own messages
          if (message.author === botId) return;
          
          console.log('Message received:', message.content);
          
          // Get channel details to check if it's a DM
          let isDM = false;
          try {
            const { data: channelData } = await axios.get(`${REVOLT_API_URL}/channels/${message.channel}`, {
              headers: { 'x-bot-token': REVOLT_TOKEN }
            });
            isDM = channelData.channel_type === 'DirectMessage';
            console.log('Channel type:', channelData.channel_type, 'isDM:', isDM);
          } catch (err) {
            console.error('Error checking channel type:', err.message);
          }
          
          // Check if bot is mentioned or if it's a DM
          const isMentioned = message.content && message.content.includes(`<@${botId}>`);
          
          if (isMentioned || isDM) {
            console.log(isDM ? 'Message is in DM' : 'Bot was mentioned!');
            try {
              // Remove the mention from the message if present
              let content = message.content;
              if (isMentioned) {
                content = content.replace(new RegExp(`<@${botId}>`, 'g'), '').trim();
              }
              
              if (!content) {
                await sendMessage(message.channel, "Hello! How can I help you today?");
                return;
              }
              
              console.log('Sending to Shapes API:', content);
              
              // Call the Shapes API
              const response = await axios.post(
                SHAPES_API_URL,
                {
                  model: `shapesinc/${SHAPES_USERNAME}`,
                  messages: [
                    { role: 'user', content: content }
                  ],
                  temperature: 0.7,
                  max_tokens: 1000
                },
                {
                  headers: {
                    'Authorization': `Bearer ${SHAPES_API_KEY}`,
                    'Content-Type': 'application/json'
                  }
                }
              );
              
              // Extract response
              const aiResponse = response.data.choices[0].message.content;
              console.log('AI Response:', aiResponse);
              
              // Send the response back to the user
              await sendMessage(message.channel, aiResponse);
              
            } catch (error) {
              console.error('Error processing message:', error.message);
              if (error.response) {
                console.error('API Response:', error.response.data);
              }
              await sendMessage(message.channel, "Sorry, I encountered an error while processing your request.");
            }
          }
        }
      } catch (err) {
        console.error('Error parsing WebSocket message:', err);
      }
    });
    
    socket.on('error', (error) => {
      console.error('WebSocket error:', error);
    });
    
    socket.on('close', (code, reason) => {
      console.log(`WebSocket connection closed: ${code} - ${reason}`);
      console.log('Reconnecting in 5 seconds...');
      setTimeout(startBot, 5000);
    });
    
  } catch (error) {
    console.error('Error starting bot:', error.message);
    if (error.response) {
      console.error('API Response:', error.response.data);
    }
    console.log('Retrying in 10 seconds...');
    setTimeout(startBot, 10000);
  }
}

// Helper function to send a message to a channel
async function sendMessage(channelId, content) {
  try {
    const response = await axios.post(`${REVOLT_API_URL}/channels/${channelId}/messages`, 
      { content },
      { headers: { 'x-bot-token': REVOLT_TOKEN } }
    );
    console.log('Message sent successfully');
    return response.data;
  } catch (error) {
    console.error('Error sending message:', error.message);
    if (error.response) {
      console.error('API Response:', error.response.data);
    }
  }
}

// Start the bot
console.log('Starting bot...');
startBot();
