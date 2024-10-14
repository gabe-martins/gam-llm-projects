import os
import json
from dotenv import load_dotenv, find_dotenv

from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory

load_dotenv(find_dotenv())

GROQ_API_KEY = os.getenv('GROQ_API_KEY', '_')
MODEL = ChatGroq(model="llama-3.1-70b-versatile")

store = {}
config = {"configurable": {"session_id": "abc123"}}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

message_history = RunnableWithMessageHistory(MODEL, get_session_history)

print('Diga algo:')
while True:
    answer = input()
    response = message_history.invoke(
        [HumanMessage(content=answer)],
        config=config,
    )
    print(response.content, end='\n')
    
    if answer == 'sair':
        break