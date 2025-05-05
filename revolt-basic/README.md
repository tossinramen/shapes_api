# Revolt Basic

A simple chat bot for [Revolt](https://revolt.chat) that uses the Shapes API to generate responses when mentioned or messaged in DMs.

## Features

- Responds to mentions in channels with AI-generated messages
- Automatically handles direct messages
- Connects to the Revolt Websocket API for real-time communication
- Uses Shapes API for AI-powered responses

## Prerequisites

- Node.js (18+) and npm
- A Revolt bot token (create one from the [Revolt Developer Portal](https://developers.revolt.chat))
- A Shapes API key

## Setup

1. Clone this repository
2. Navigate to the revolt-basic directory:
   ```
   cd revolt-basic
   ```
3. Install dependencies:
   ```
   npm install
   ```
4. Create a `.env` file from the example:
   ```
   cp .env.example .env
   ```
5. Edit the `.env` file and add your credentials:
   ```
   REVOLT_TOKEN=your-revolt-bot-token
   SHAPESINC_API_KEY=your-shapes-api-key
   SHAPESINC_SHAPE_USERNAME=your-shape-username
   ```

## Usage

1. Start the bot:
   ```
   npm start
   ```

2. In any Revolt channel where the bot is present, tag the bot followed by your message:
   ```
   @BotName How are you today?
   ```

3. You can also DM the bot directly, and it will respond to all messages.

## How it Works

The bot uses the Revolt WebSocket API to receive real-time messages. When it detects a mention or a DM, it:

1. Extracts the user's message
2. Sends the message to the Shapes API
3. Returns the AI-generated response back to the Revolt chat

## Customization

You can customize which shape personality is used by changing the `SHAPESINC_SHAPE_USERNAME` in your `.env` file. 