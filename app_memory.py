from fastapi import FastAPI
from pydantic import BaseModel
from analytics.data_loader import load_user_data
from analytics.behavior_engine import summarize_user_behavior
from llm.suggestion_engine import get_suggestion
from memory.memory_store import init_db, get_user_memory, save_user_memory
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Allow CORS for all origins (during development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to ["http://localhost:3000"] etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def serve_chat_ui(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

init_db()

class UserRequest(BaseModel):
    user_id: str
    question: str | None = None

@app.post("/suggest/")
def suggest_action(req: UserRequest):
    user_id = req.user_id
    question = req.question

    # Load current behavior
    user_sessions = load_user_data(user_id)
    if not user_sessions:
        behavior_summary = "No previous product interactions"
    
    else:
        behavior_summary = summarize_user_behavior(user_sessions)

    # Commenting out this block, this would be used in production where 
    # there's past sessions and current data to draw from
    #
    # Load previous memory (if any)
    # memory = get_user_memory(user_id)
    # memory_text = f"Past summary: {memory['behavior_summary']}. Last suggestion: {memory['last_suggestion']}" if memory else "No prior memory."

    # Ask LLM with combined context
    suggestion = get_suggestion(
        context=question,
        user_id=user_id,
        behavior_summary=behavior_summary
    )

    # Save updated memory
    save_user_memory(user_id, behavior_summary, suggestion)

    return {"suggestion": suggestion}
