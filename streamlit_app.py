from urllib import response
import streamlit as st
import os
from dotenv import load_dotenv, find_dotenv

from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq

load_dotenv(find_dotenv())

GROQ_API_KEY = os.getenv('GROQ_API_KEY', '_')

# Configuracao da pagina
st.set_page_config(page_title="IN-Chat", layout="wide", page_icon="./components/images/favicon.ico")
# st.title("💬 Chatbot")
# st.caption("powered Groq")

# Chat memory
msgs = StreamlitChatMessageHistory(key="langchain_messages")
if len(msgs.messages) == 0:
  msgs.add_ai_message("Como posso te ajudar?")
  
prompt = ChatPromptTemplate.from_messages(
  [
    ("system", "Você é um chatbot de IA conversando com um humano."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
  ]
)

options = ["llama-3.2-90b-text-preview", "llama3-groq-70b-8192-tool-use-preview", "gemma2-9b-it", "llama3-70b-8192"]
selecao = st.selectbox('Select a model...', options)

chain = prompt | ChatGroq(model=selecao)
chain_with_history = RunnableWithMessageHistory(
  chain,
  lambda session_id: msgs,
  input_messages_key="question",
  history_messages_key="history",
)

for msg in msgs.messages:
  st.chat_message(msg.type).write(msg.content)
  
if prompt := st.chat_input("Diga algo"):
  st.chat_message("human").write(prompt)      
  config = {"configurable": {"session_id": "any"}}          
  response = chain_with_history.invoke({"question": prompt}, config)
  st.chat_message("ai").write(response.content)
