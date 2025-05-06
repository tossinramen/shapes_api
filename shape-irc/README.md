# Advanced Python examples for the Shapes API

## Prerequisites

- Python 3.12+
- pip
- virtualenv

## Setup

```bash
./setup.sh
```

This will create a virtual environment and install the required dependencies.

## Usage

Copy the `.env.example` file to `.env` and add your API keys.

```bash
source venv/bin/activate
python main.py --channel IRC_CHANNEL --server IRC_SERVER [--shape SHAPE_NAME]
```

### Command Line Arguments

TODO

### Examples

```bash
# Basic usage with a message
python main.py --channel foobar --server irc.libera.chat
```

------------------
© 2025 Shapes Inc.
