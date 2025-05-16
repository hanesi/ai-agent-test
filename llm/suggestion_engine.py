import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load your API key from a .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_suggestion(behavior_summary: str) -> str:
    prompt = f"""
    A user has recently done the following: {behavior_summary}
    What are 1–2 helpful or engaging actions they might want to do next?
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a helpful product assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']
