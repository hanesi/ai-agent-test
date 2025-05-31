# ai-agent-test

# How It Works:

- Loads mock session data for a user.
- Creates a summary of their previous session
- Sends a behavior summary to GPT-3.5.
- Returns actionable suggestions.
- Updates memory DB

## Install dependencies
```
pip install -r requirements.txt
```

## Add your OpenAI API key
Create a file named .env in the root directory and add:

`OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

## Start the FastAPI server:

`uvicorn app_memory:app --reload`

## Test in browser

Navigate to http://127.0.0.1:8000 and chat!

# Video Demo


https://github.com/user-attachments/assets/ea6201dd-a245-4712-bee7-5a92e16fded6

