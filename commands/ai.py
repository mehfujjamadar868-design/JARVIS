import os
# Used to read the Gemini API key

from dotenv import load_dotenv
# Used to load the .env file

from google import genai
# Used to connect Python with Gemini


load_dotenv()
# Loads variables from the .env file

api_key = os.getenv("GEMINI_API_KEY")
# Gets the Gemini API key securely

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")
# Stops the program if the API key is missing

client = genai.Client(api_key=api_key)
# Creates the Gemini API client


def ask_ai(prompt):
    # Sends a prompt to Gemini and returns the answer

    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=prompt
    )
    # Sends the prompt to Gemini using the Interactions API

    return interaction.output_text
    # Returns Gemini's text response
