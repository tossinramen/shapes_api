Build AI friends and coworkers in Slack


How I created an AI friend for my slack workspace using shapes.inc

We will be creating a slack app that will be able to read messages in a channel and reply to them in the ui. 

Here's how we will implement this:
1. Create a Slack app that can listen to messages in channels
2. Set up event subscriptions to capture messages
3. Process these messages through your API, which is hooked up the the Shapes API
4. Use the Slack API to post responses back to the channel
Let me walk you through the implementation approach:


Setting Up Your Slack App
You'll need to create a Slack app with the right permissions to:
1. Read messages in channels (without being mentioned)
2. Post messages back to channels
Here's how to build this:


Step 1: Create a Slack App
First, you'll need to create a Slack App with the proper permissions:
1. Go to https://api.slack.com/apps and click "Create New App" > "From scratch"
2. Enter a name for your app and select your workspace
3. Once created, you'll need to set up permissions and event subscriptions

Step 2: Configure Bot Permissions
Under the "OAuth & Permissions" section, add these bot token scopes:
* channels:history - To read messages in channels
* chat:write - To send messages as your bot

Step 3: Set Up Event Subscriptions
This is the critical part for detecting messages without being mentioned:
1. Go to "Event Subscriptions" in your app's settings and enable events
2. Add the Request URL where your server will receive events (e.g., https://your-api.example.com/slack/events)
3. Under "Subscribe to bot events," add the message.channels event type
    * This lets your bot receive all messages from public channels it's in without requiring mentions Slack API

Step 4: Install App to Workspace
After configuring permissions, install your app to your workspace. You'll receive a Bot User OAuth Token that you'll need for your application.

Step 5: Create Your Backend API
Now you'll need to create a server to process messages and send replies.


How it works:

User sends a message in a Slack channel where your bot is a member
Slack sends this event to your server at /slack/events
app receives this event
It processes the message using the integrated Shapes API client
It sends the response back to the Slack channel
