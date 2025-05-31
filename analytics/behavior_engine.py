def summarize_user_behavior(user_sessions):
    all_actions = [action for session in user_sessions for action in session['actions']]
    summary = f"Here is a summary of the user's previous session: \n - {'\n - '.join(i for i in all_actions)}"
    return summary
