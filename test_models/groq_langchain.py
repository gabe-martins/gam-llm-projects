from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

template = """
Você é um engenheiro de software trabalhando na documentacao de um codigo. 
retorne as explicacoes mais breves possiveis sobre os codigos informadados. 
{text}

Responda apenas com a explicacao. 
""" 

prompt = PromptTemplate.from_template(template=template)

# Groq
chat = ChatGroq(model="llama-3.1-70b-versatile")
chain = prompt | chat | StrOutputParser()

chain.invoke("select * from table_one")