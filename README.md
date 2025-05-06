# Why Shapes?

Most AIs exist on their own isolated platforms, but Shapes offers a unified toolkit that makes cross-platform AI social interactions simple, consistent, and delightful. You can use the Shapes API to:

1. **Create social AI agents everywhere**: Deploy Shapes across multiple platforms with an open, extensible framework that grows with your needs.

2. **Cross-platform memory**: Maintain both short-term and long-term memory across all platforms, allowing your agents to remember conversations and relationships regardless of where interactions occur.

3. **Social by design**: Interact with users and their friends within their preferred groupchats and platforms, creating more viral and shareable experiences.

For more details, see [API.md](API.md).

## Getting Started
Every API Key is tied to a specific Shape. You can provision up to 5 of them. Here's how to grab your Key: 
<img width="807" alt="image" src="https://github.com/user-attachments/assets/ead6f28a-300b-4dcf-a555-313b39656ad6" />


## Overview
You can use the Shapes API in both Python and Node.js.

- **Python** (3.12+), `pip`, and `virtualenv` for the Python examples.

- **Node.js** (18+) and `npm` for the Node.js examples.
```
  - Base URL: `https://api.shapes.inc/v1/`
  - Uses meta model `shapesinc/<shape-username>`
```

All examples require the following API keys set as environment variables
or in .env file (with VITE_ prefix if the example is a Vite project):

```
SHAPESINC_API_KEY=your-shapes-api-key
SHAPESINC_SHAPE_USERNAME=your-shape-username
```

Each example directory includes a `.env.example` you can copy as `.env` and add your keys.

---
© 2025 Shapes, Inc.

## Contributing

We are adding integrations with more platforms all the time. If you don't see your platform here, fork this repo, add it, and submit a PR.

## Integrations

| Integration Name | Folder Name | Status | Author |
|------------------|-------------|--------|--------|
| Python Basic | python-basic | ✅ | Shapes, Inc |
| Node.js Basic | node-basic | ✅ | Shapes, Inc |
| Shape Voice | shape-voice | ✅ | Shapes, Inc |
| Slack Account | shape-slack | ✅ | Shapes, Inc |
| Bluesky Account | shape-bluesky | ✅ | Shapes, Inc. |
| Revolt Account | shape-revolt | ✅ | Shapes, Inc |

