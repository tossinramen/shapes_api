import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

async def main():
    # Depending on the shape personality and the history, this messge might trigger various reactions
    messages = [
        {
            "role": "user",
            "content": "Hello. What's your name?",
        }
    ]

    try:
        # Check for SHAPESINC_SHAPE_API_KEY in .env
        if not os.getenv("SHAPESINC_SHAPE_API_KEY"):
            raise ValueError("SHAPESINC_SHAPE_API_KEY not found in .env")

        # Create the client with the shape API key and the Shapes API base URL
        aclient_shape = AsyncOpenAI(
            api_key=os.getenv("SHAPESINC_SHAPE_API_KEY"),
            base_url="https://api.shapes.inc/formless/",
        )

        # Send the message to the shape. This will use the shape configured model.
        # WARNING: If the shape is premium, this will also consume credits.
        resp = await aclient_shape.chat.completions.create(
            model="shapesinc/shapes-api",
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
