from collections import Counter

def summarize_user_behavior(user_sessions):
    all_actions = [action for session in user_sessions for action in session['actions']]
    action_counts = Counter(all_actions)
    summary = f"Top actions: {action_counts.most_common(3)}"
    return summary
