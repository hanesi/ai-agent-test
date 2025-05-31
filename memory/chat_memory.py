from typing import Dict, List
from langchain.schema import BaseMessage

# Simple in-memory store (replace with Redis, database, or disk later)
_chat_memory_store: Dict[str, List[BaseMessage]] = {}

def load_chat_history(user_id: str) -> List[BaseMessage]:
    return _chat_memory_store.get(user_id, [])

def save_chat_history(user_id: str, history: List[BaseMessage]):
    _chat_memory_store[user_id] = history

def clear_chat_history(user_id: str):
    _chat_memory_store.pop(user_id, None)
