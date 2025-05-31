from openai import OpenAI
import os
from dotenv import load_dotenv
from .llm_constants import SYSTEM_PROMPT, BASE_PROMPT
from memory.chat_memory import load_chat_history, save_chat_history

from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

chat = ChatOpenAI(temperature=0.1, model_name="gpt-3.5-turbo", verbose=True)

def get_suggestion(context: str, user_id: str, behavior_summary: str) -> str:
    message_history = load_chat_history(user_id)

    if not message_history:
        prompt = BASE_PROMPT.format(behavior_summary=behavior_summary)
        message_history.append(SystemMessage(content=SYSTEM_PROMPT))
        message_history.append(HumanMessage(content=prompt))

    else:
        message_history.append(HumanMessage(content=context))

    response = chat.invoke(message_history)

    message_history.append(AIMessage(content=response.content))
    save_chat_history(user_id, message_history)

    return response.content

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def get_suggestion(behavior_summary: str) -> str:
#     prompt = BASE_PROMPT.format(behavior_summary=behavior_summary)

#     response = client.chat.completions.create(model="gpt-4",
#     messages=[
#         {"role": "system", "content": SYSTEM_PROMPT},
#         {"role": "user", "content": prompt}
#     ])
#     return response.choices[0].message.content
