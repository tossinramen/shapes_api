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

Add a pfp for your app under "Display Information"

Get your tokens

SLACK_BOT_TOKEN

Go to the Slack API Dashboard and sign in with your Slack account
Select your Slack app from the list (or create a new one if you haven't already)
In the left sidebar, click on "OAuth & Permissions"
Look in the "Bot User OAuth Token" section at the top of the page
The token will start with xoxb-

This token is what your app will use to authenticate with Slack's API. It provides the permissions you've configured for your bot, such as reading messages and posting responses.

SLACK_SIGNING_SECRET

In the "Basic Information" section of your Slack app settings
Under "App Credentials"
It's listed as "Signing Secret"

Make sure to keep these credentials secure and never commit them to public repositories. It's best practice to use environment variables as you're doing with Heroku's config settings.

Step 2: Configure Bot Permissions
Under the "OAuth & Permissions" section, add these bot token scopes:

- channels:history - To read messages in channels
- chat:write - To send messages as your bot

Step 3: Set Up Event Subscriptions (only do this when app is deployed - see deployment section)
This is the critical part for detecting messages without being mentioned:

1. Go to "Event Subscriptions" in your app's settings and enable events
2. Add the Request URL where your server will receive events (e.g., https://your-api.example.com/slack/events)
3. Under "Subscribe to bot events," add the message.channels event type
   - This lets your bot receive all messages from public channels it's in without requiring mentions Slack API

Step 4: Install App to Workspace
After configuring permissions, install your app to your workspace. You'll receive a Bot User OAuth Token that you'll need for your application.

Step 5: Create Your Backend API
Now you'll need to create a server to process messages and send replies.

You can use the app.py file as a starting point. All you need to do is create a simple server that will pickup slack events, you use the shapes client to process the message and then send the response back to slack using the slack bolt framework.

How it works:

User sends a message in a Slack channel where your bot is a member
Slack sends this event to your server at /slack/events
app receives this event
It processes the message using the integrated Shapes API client
It sends the response back to the Slack channel

Run it locally:

```
pip install -r requirements.txt
python app.py
```

Deploy it to heroku:

0. Install tar

```
brew install gnu-tar
```

1. Install the Heroku CLI
   If you haven't already, install the Heroku CLI following the instructions on the Heroku Dev Center.

Login to Heroku

```
heroku login
```

# Install the builds plugin

This is needed to deploy the app to heroku without using git.

```
heroku plugins:install heroku-builds
```

# Create the app

After you have verified your [account on heroku](https://devcenter.heroku.com/articles/account-verification), create the app. I called mine slack-basic.

Set Environment Variables

```
heroku config:set SLACK_BOT_TOKEN=xoxb-your-bot-token --app slack-basic
heroku config:set SLACK_SIGNING_SECRET=your-signing-secret --app slack-basic
heroku config:set SHAPESINC_SHAPE_API_KEY=your-shapes-api-key --app slack-basic
heroku config:set SHAPESINC_SHAPE_USERNAME=your-shapes-username --app slack-basic
```

# Deploy from current directory

```
heroku builds:create --app slack-basic --tar=node
```

You should see your app live from a url that looks like this

https://slack-basic-385173ecf3f7.herokuapp.com/

# Verify your app for slack

Now that your app is live (on Heroku or platform of choice), you can verify it for slack.

1. Go to the Slack API Dashboard and sign in with your Slack account
2. Select your Slack app from the list (or create a new one if you haven't already)
3. In the left sidebar, click on "Event Subscriptions"
4. Under "Enable Events", enter the url of your app with the /slack/events endpoint

This is mine:

```
https://slack-basic-385173ecf3f7.herokuapp.com/slack/events
```

5. Under "Subscribe to bot events", add the message.channels event type

```
message.channels
```

6. Click "Save Changes"


Now unleash your Shape!

Step 1: Invite Your Bot to a Channel

In your Slack workspace, create a test channel or use an existing one
Invite your bot by typing /invite @your-bot-name in the channel

Step 3: Send a Test Message

Send a simple message in the channel where your bot was invited
Your message should be picked up by your bot even without mentioning it directly

Step 4: Check the Logs

Monitor your Heroku logs to see if your bot is receiving the events:
heroku logs --tail --app slack-basic-385173ecf3f7

Look for log entries showing the received message event
