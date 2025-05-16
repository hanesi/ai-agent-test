# ai-agent-test

Install dependencies
```
pip install -r requirements.txt
```

Add your OpenAI API key
Create a file named .env in the root directory and add:
`OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

Start the FastAPI server:
`uvicorn app:app --reload`

Request
`POST http://localhost:8000/suggest/`

Body
```
{
  "user_id": "user_1"
}
```

Response:
```
{
  "suggestion": "You might want to check your cart or explore new features in the dashboard."
}
```

How It Works:
- Loads mock session data for a user.
- Analyzes their most common actions.
- Sends a behavior summary to GPT-4.
- Returns actionable suggestions.
