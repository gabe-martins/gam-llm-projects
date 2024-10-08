from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from dotenv import load_dotenv, find_dotenv
import os
import pandas as pd

load_dotenv(find_dotenv())
GROQ_API_KEY = os.getenv('GROQ_API_KEY', '_')
BASE_DB_PATH = '../databases/'

template = """
Você é um administrador de banco de dado trabalhando na monitoria das queries em execucao. 
retorne as tabelas que cada query esta consumindo.. 
{text}

Responda apenas com as tabelas em forma de lista separada por virgula. 
""" 

df = pd.read_csv(BASE_DB_PATH + 'raw_queries.csv')

# LLM ==================================================
prompt = PromptTemplate.from_template(template=template)

chat = ChatGroq(model="llama-3.1-70b-versatile")
chain = prompt | chat | StrOutputParser()

description = []
for query in list(df["Query SQL"].values):
  print(query)
  description += [chain.invoke(query)]

df["Tabelas Usadas"] = description
df.to_csv(BASE_DB_PATH + 'processed_queries.csv', index=False, header=True, sep=',')