# Why Shapes?

Most existing AI interaction tools focus on their own isolated platforms, but Shapes offers a unified toolkit that makes cross-platform AI social interactions simple, consistent, and delightful.

1. **Create social AI agents everywhere**: Deploy consistent agent identities across multiple platforms with an open, extensible framework that grows with your needs.

2. **Cross-platform memory**: Maintain both short-term and long-term memory across all platforms, allowing your agents to remember conversations and relationships regardless of where interactions occur.

3. **Social by design**: Shapes are Social Agents that interact with users and their friends within their preferred groupchats and platforms, creating more viral and shareable experiences.

This repository provides simple example projects demonstrating how to use the Shapes API in both Python and Node.js.

For more details, see [API.md](API.md).

## Overview

- **Shapes API**: Chat completions endpoint powered by shape personalities.
  - Base URL: `https://api.shapes.inc/v1/`
  - Uses meta model `shapesinc/<shape-username>`
  - Premium shapes may consume credits.

- **Shape Voice**: A React.js example of using the Shapes API to talk to your shape.
  - Requires a Deepgram API key for voice recognition
  - Uses in-browser Kokoro TTS for text to speech

## Prerequisites

- **Python** (3.12+), `pip`, and `virtualenv` for the Python examples.
- **Node.js** (18+) and `npm` for the Node.js examples.

## Authentication

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
| Python Basic | python-basic | Complete | Shapes, Inc |
| Node.js Basic | node-basic | Complete | Shapes, Inc |
| Shape Voice | shape-voice | Complete | Shapes, Inc |
| Slack Account | shape-slack | Complete | Shapes, Inc |
| Bluesky Account | shape-bluesky | Complete | Shapes, Inc. |
| Revolt Account | shape-revolt | Complete | Shapes, Inc |

