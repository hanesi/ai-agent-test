from fastapi import FastAPI
from pydantic import BaseModel
from analytics.data_loader import load_user_data
from analytics.behavior_engine import summarize_user_behavior
from llm.suggestion_engine import get_suggestion
from memory.memory_store import init_db, get_user_memory, save_user_memory

app = FastAPI()
init_db()

class UserRequest(BaseModel):
    user_id: str

@app.post("/suggest/")
def suggest_action(req: UserRequest):
    user_id = req.user_id

    # Load current behavior
    user_sessions = load_user_data(user_id)
    if not user_sessions:
        return {"suggestion": "No data available for this user."}
    
    behavior_summary = summarize_user_behavior(user_sessions)

    # Load previous memory (if any)
    memory = get_user_memory(user_id)
    memory_text = f"Past summary: {memory['behavior_summary']}. Last suggestion: {memory['last_suggestion']}" if memory else "No prior memory."

    # Ask LLM with combined context
    suggestion = get_suggestion(f"{memory_text}\n\nCurrent: {behavior_summary}")

    # Save updated memory
    save_user_memory(user_id, behavior_summary, suggestion)

    return {"suggestion": suggestion}
