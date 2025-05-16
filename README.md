# ai-agent-test

# How It Works:

- Loads mock session data for a user.
- Analyzes their most common actions.
- Checks SQLite DB for past user interactions/suggestions
- Sends a behavior summary to GPT-4.
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

`uvicorn app:app --reload`

## Test Request (using python)

```
import requests

url = "http://localhost:8000/suggest/"

payload = {
    "user_id": "user_1"
}

response = requests.post(url, json=payload)
print("Response JSON:", response.json())
```

Response should resemble something like this:
```
{
  "suggestion": "You might want to check your cart or explore new features in the dashboard."
}
```

