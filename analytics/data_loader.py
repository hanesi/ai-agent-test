import json

def load_user_data(user_id: str, path: str = "mock_data/mock_analytics.json"):
    with open(path) as f:
        all_data = json.load(f)
    user_sessions = [s for s in all_data if s['user_id'] == user_id]
    return user_sessions
