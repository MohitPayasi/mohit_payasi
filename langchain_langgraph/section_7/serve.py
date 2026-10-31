from fastapi import FastAP
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['GROQ_API_KEY']= os.getenv('GROQ_API_KEY')
from langchain_groq import ChatGroq
llm=ChatGroq(model='openai/gpt-oss-20b')
generic_template= 'translate the following into {langauge}'
prompt= ChatPromptTemplate.from_messages([
    ('system', generic_template),('user',"{text}")
])






















