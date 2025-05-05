import os
import sys
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletion

load_dotenv()


async def main():
    # If the user provided a message on the command line, use that one
    args = sys.argv[1:]
    if args:
        messages = [
            {
                "role": "user",
                "content": " ".join(args),
            }
        ]
    else:
        # Depending on the shape personality and the history, this messge might trigger various reactions
        messages = [
            {
                "role": "user",
                "content": "Hello. What's your name?",
            }
        ]

    try:
        shape_api_key = os.getenv("SHAPESINC_API_KEY")
        shape_username = os.getenv("SHAPESINC_SHAPE_USERNAME")

        # Check for SHAPESINC_API_KEY in .env
        if not shape_api_key:
            raise ValueError("SHAPESINC_API_KEY not found in .env")

        # Check for SHAPESINC_SHAPE_USERNAME in .env
        if not shape_username:
            raise ValueError("SHAPESINC_SHAPE_USERNAME not found in .env")

        # Create the client with the shape API key and the Shapes API base URL
        aclient_shape = AsyncOpenAI(
            api_key=shape_api_key,
            base_url="https://api.shapes.inc/v1/",
        )

        # Send the message to the shape. This will use the shape configured model.
        # WARNING: If the shape is premium, this will also consume credits.
        resp: ChatCompletion = await aclient_shape.chat.completions.create(
            model=f"shapesinc/{shape_username}",
            messages=messages,
        )
        print(f"Raw response: {resp}")

        if resp.choices and len(resp.choices) > 0:
            final_response = resp.choices[0].message.content
            print(f"Reply: {final_response}")
        else:
            print(f"No choices in response: {resp}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
