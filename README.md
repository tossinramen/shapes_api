# Shapes Inc. Basic API Examples

This repository provides simple example projects demonstrating how to use the Shapes Inc. Formless and Shapes APIs in both Python and Node.js.

## Overview
- **python-basic/**: Async Python examples using the official `openai` Python SDK.
- **nodejs-basic/**: ESM Node.js examples using the official `openai` JavaScript SDK.

## APIs
- **Formless API**: Chat completions endpoint for general-purpose LLM interactions.
  - Base URL: `https://api.shapes.inc/formless/`
  - Model: `shapesinc/Formless-70B-v1a`
- **Shapes API**: Chat completions endpoint powered by shape personalities.
  - Uses meta model `shapesinc/shapes-api`
  - Premium shapes may consume credits.

## Prerequisites
- **Python** (3.12+), `pip`, and `virtualenv` for the Python examples.
- **Node.js** (18+) and `npm` for the Node.js examples.

## Authentication
Both examples require two API keys set as environment variables:

```
SHAPESINC_USER_API_KEY=your_user_api_key_here
SHAPESINC_SHAPE_API_KEY=your_shape_api_key_here
```

Each example directory includes a `.env.example` you can copy as `.env` and add your keys.

---
© 2025 Shapes Inc.