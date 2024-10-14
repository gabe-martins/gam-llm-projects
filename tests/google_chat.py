# import streamlit as st
from dotenv import load_dotenv, find_dotenv
import os
import google.generativeai as genai

load_dotenv(find_dotenv())

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '.')
genai.configure(api_key=GEMINI_API_KEY)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Você é um administrador de banco de dado trabalhando na monitoria das queries em execucao.\nretorne as tabelas que cada query esta consumindo..\nSELECT * FROM [Tabela_Compras];\n\nResponda apenas com as tabelas em forma de lista separada por virgula.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "[Tabela_Compras] \n",
      ],
    },
  ]
)

print(chat_session.send_message(input()).text)