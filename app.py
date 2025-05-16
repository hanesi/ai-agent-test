from fastapi import FastAPI
from pydantic import BaseModel
from analytics.data_loader import load_user_data
from analytics.behavior_engine import summarize_user_behavior
from llm.suggestion_engine import get_suggestion

app = FastAPI()

class UserRequest(BaseModel):
    user_id: str

@app.post("/suggest/")
def suggest_action(req: UserRequest):
    user_sessions = load_user_data(req.user_id)
    if not user_sessions:
        return {"suggestion": "No data available for this user."}
    
    behavior_summary = summarize_user_behavior(user_sessions)
    suggestion = get_suggestion(behavior_summary)
    
    return {"suggestion": suggestion}
