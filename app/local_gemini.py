from dotenv import load_dotenv, find_dotenv
import os
import json
import google.generativeai as genai

load_dotenv(find_dotenv())

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '.')
genai.configure(api_key=GEMINI_API_KEY)

with open('../databases/history-20241014-15200-12345.json', 'r', encoding='utf-8') as arquivo: 
  chat_history = json.load(arquivo)
  
def write_chat_history(answer, response):
  chat_history.append({'role': 'user', 'parts': list(answer)})
  chat_history.append({'role': 'model', 'parts': list(response)})
  
  return chat_history

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
  history=chat_history
)

while True:
  answer = input()
  response = chat_session.send_message(answer)
  print(response.text)
  
  chat_history = write_chat_history(answer, response.text)
  
  if answer.lower() == 'sair':
    break
  
print(chat_history)