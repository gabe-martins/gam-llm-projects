from dotenv import load_dotenv, find_dotenv
import os
import json
import google.generativeai as genai
import mongo_conn as db_con

load_dotenv(find_dotenv())

chat_history = db_con.get_chat_history()

def write_chat_history(answer="-", response="."):
  chat_history.append({'role': 'user', 'parts': [answer]})
  chat_history.append({'role': 'model', 'parts': [response]})
  db_con.write_chat_history(chat_history)
  
  return chat_history

# Create the model
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '.')
genai.configure(api_key=GEMINI_API_KEY)

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
  history=chat_history
)

while True:
  chat_history = []
  answer = input("> ").replace("> ", "")
  response = chat_session.send_message(answer)
  print(response.text)
  
  chat_history = write_chat_history(answer, response.text)
  
  if answer.lower() == 'sair':
    break