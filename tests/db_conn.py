import os
import json
from unittest import result
import pymongo
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGO_USER = os.getenv('MONGO_USER', '_')
MONGO_PASS = os.getenv('MONGO_PASS', '_')
MONGO_URL = f'mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cls-pandora.rh9xl.mongodb.net/?retryWrites=true&w=majority&appName=cls-pandora'

client = pymongo.MongoClient(MONGO_URL)
db = client['in-chat']
coll = db['messages']

def store_messages(messages):
  result = coll.insert_one(messages)
  print(result)
  print(list(coll.find()))