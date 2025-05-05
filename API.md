## What is the Shapes API?

Shapes API is a programmatic way to talk to your shapes.

### Shape Platforms

The Shapes API can be used to talk to your shape, whether or not they are connected on other platforms. You can have your shape in a Telegram bot, and also talk to it through your own application.

### Credit use

NOTE: Premium shapes *WILL* use credits.
This is no different than using your premium shape on platforms like X. So plan accordingly.

### Limitations

Since Shapes APi will rely on the model the shape is configured with, we cannot support all features that a regular OpenAI compatible API would support.

In particular, Shapes API will not support initially:

* System/developer role message \- these are already part of the shape settings
* Multiple messages/message history \- for now we rely on the Shape memory for this, no need to specify these. Essentially, we ignore all other messages except the last role=”user” message in the request.
* Streaming requests \- for now shapes API will be limited to non-streaming responses only
* Tool calls \- not all models support tool calls. We might enable this for specific models later
* Temperature, and other parameters that can be sent normally \- this is to prevent unwanted changes to the shape personality as configured in the shape settings

### Rate limits

To ensure stability of the shapes, the Shapes API will be heavily rate limited. If the standard limits don't work for you, we can increase those on a shape-by-shape basis, to ensure a smooth experience for all users of the shape.

## How to use the Shapes API?

### Model name

The model names used for Shapes API are in the form of `shapesinc/<shape-username>`. For example, if your shape username is `archibald-brave`, the model name to use the API with the shape would be `shapesinc/archibald-brave`.

Using the external model name above does not affect the model you selected when you created the shape. Internally, your shape will still use the same base model you configured for it.

### API Endpoints

We support OpenAI-compatible API endpoint that can be used with the OpenAI Python or Javascript client SDKs. The API supports only non-streaming requests.

### Base URL

`https://api.shapes.inc/v1`

### Endpoints

- Chat Completions: `/chat/completions`

### Authentication

Authentication is done via API key. The API key is passed in the `Authorization` header as a Bearer token.

### Rate limiting

We are still working through the specifics of the exact rate limits, so there are no hard numbers. But we want to ensure that our API and morels scale well, so might throttle API calls from time to time.

### Examples

You can find more examples in [https://github.com/shapesinc/api-examples](https://github.com/shapesinc/api-examples)

All examples use the same shape username and API key. Replace `<your-API-key>` and `<shape-username>` with your actual API key and shape username.

#### Curl

```bash
curl -X POST https://api.shapes.inc/v1/chat/completions \
     -H "Authorization: Bearer \<your-API-key\>" \
     -H "Content-Type: application/json" \
     -d '{"model": "shapesinc/<shape-username>", "messages": [{ "role": "user", "content": "Hello" }]}'
```

#### Python

```python
import openai

shapes_client = OpenAI(
    api_key="<your-API-key>",
    base_url="https://api.shapes.inc/v1/",
)

response = shapes_client.chat.completions.create(
    model="shapesinc/<shape-username>",
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

print(response)
```

#### Javascript

```Javascript
const openai = require("openai");

const shapes_client = new OpenAI({
    apiKey: "<your-API-key>",
    baseURL: "https://api.shapes.inc/v1",
});

const response = await shapes_client.chat.completions.create({
    model: "shapesinc/<shape-username>",
    messages: [
        { role: "user", content: "Hello" }
    ]
});

console.log(response);
```

# Use Cases

### **Don’t like the official shapes discord integration? This is for you.**

- You can vibe code your own discord client and attach a shape to it (see example:)
- You can interact with the shape on Silly Tavern (see instructions on how to:)
- \[TODO\]

### **Host a shape on your own Discord Bot**

### **Interact with your shape on Silly Tavern**

# Request for Apps

- An app that allows your shape to be a reddit bot
- An app that allows your shape to code review your Github PRs
- An app that allows you to email shapes
- An app that allows you to chat with shapes on Whatsapp
- An app that allows you to chat with shapes on Instagram
- An app that allows you to chat with shapes on Facebook
- An app that allows you to iMessage with shapes
- An app that allows you to SMS shapes
- \[Todo\]