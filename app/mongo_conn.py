import os
import json
from unittest import result
import pymongo
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGO_USER = os.getenv('MONGO_USER', '_')
MONGO_PASS = os.getenv('MONGO_PASS', '_')

MONGO_URL = f'mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cls-pandora.rh9xl.mongodb.net/in-chat?retryWrites=true&w=majority&appName=cls-pandora'

client = pymongo.MongoClient(MONGO_URL)
db = client['chat-history']

def get_chat_history(chat_id="670e749d214ef2458bad0f34"):
  coll = db[chat_id]  
  chat_history = list(coll.find({}, {"_id": 0}))
  return chat_history

def write_chat_history(chat_history, chat_id="670e749d214ef2458bad0f34"):
  coll = db[chat_id]
  coll.insert_many(chat_history)