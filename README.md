# Shapes Inc. Basic API Examples

This repository provides simple example projects demonstrating how to use the Formless and Shapes APIs in both Python and Node.js.

## Overview

- **Formless API**: Chat completions endpoint for general-purpose LLM interactions.
  - Base URL: `https://api.shapes.inc/formless/`
  - Model: `shapesinc/Formless-70B-v1a`
- **Shapes API**: Chat completions endpoint powered by shape personalities.
  - Uses meta model `shapesinc/shapes-api`
  - Premium shapes may consume credits.
- **Shape Voice**: A React.js example of using the Shapes API to talk to your shape.
  - Requires a Deepgram API key for voice recognition
  - Uses in-browser Kokoro TTS for text to speech

## Prerequisites

- **Python** (3.12+), `pip`, and `virtualenv` for the Python examples.
- **Node.js** (18+) and `npm` for the Node.js examples.

## Authentication

All examples require at least one of the following API keys set as environment variables
or in .env file (with VITE_ prefix if the example is a Vite project):

```
SHAPESINC_USER_API_KEY=your_user_api_key_here
SHAPESINC_SHAPE_API_KEY=your_shape_api_key_here
```

Each example directory includes a `.env.example` you can copy as `.env` and add your keys.

---
© 2025 Shapes Inc.