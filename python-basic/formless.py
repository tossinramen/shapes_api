import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

async def main():
    messages = [
        {
            "role": "user",
            "content": "Hello. What is your name?",
        }
    ]

    try:
        # Check for SHAPESINC_USER_API_KEY in .env
        if not os.getenv("SHAPESINC_USER_API_KEY"):
            raise ValueError("SHAPESINC_USER_API_KEY not found in .env")

        # Create the client with the user API key and the Formless API base URL
        aclient_formless = AsyncOpenAI(
            api_key=os.getenv("SHAPESINC_USER_API_KEY"),
            base_url="https://api.shapes.inc/formless/",
        )

        # Send the message to the Formless LLM. This will use the Formless model.
        resp = await aclient_formless.chat.completions.create(
            model="shapesinc/Formless-70B-v1a",
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
