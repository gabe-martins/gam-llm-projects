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
        "Oi",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Olá",
      ],
    },
  ]
)

while True:
  answer = input()
  response = chat_session.send_message(answer)
  print(response.text)
  
  if answer.lower() == 'sair':
    break

chat_session.history