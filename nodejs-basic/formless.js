import { config } from "dotenv";
import OpenAI from "openai";

config();

async function main() {
  try {
    // Check for SHAPESINC_USER_API_KEY in .env
    if (!process.env.SHAPESINC_USER_API_KEY) {
      throw new Error("SHAPESINC_USER_API_KEY not found in .env");
    }

    // Create the client with the user API key and the Formless API base URL
    const openai = new OpenAI({
      apiKey: process.env.SHAPESINC_USER_API_KEY,
      baseURL: "https://api.shapes.inc/formless/"
    });

    // If the user provided a message on the command line, use that one
    const args = process.argv.slice(2);
    const messages = [
      { role: "user", content: args.length > 0 ? args.join(" ") : "Hello. What is your name?" }
    ];

    // Send the message to the Formless LLM. This will use the Formless model.
    const resp = await openai.chat.completions.create({
      model: "shapesinc/Formless-70B-v1a",
      messages
    });

    console.log("Raw response:", resp);

    if (resp.choices && resp.choices.length > 0) {
      console.log("Reply:", resp.choices[0].message.content);
    } else {
      console.log("No choices in response:", resp);
    }
  } catch (error) {
    console.error("Error:", error);
  }
}

main();