

import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()
groq_api= os.getenv('GROQ_API')
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.messages     import HumanMessage,SystemMessage
model= ChatGroq(model='openai/gpt-oss-20b', api_key=groq_api)

from fastapi import FastAPI
from langserve import add_routes
app = FastAPI(
    title='LangChain Server',
    
)
prompt=ChatPromptTemplate.from_messages([
    ('system', 'You are {domain_name} content creater'),('user','{question}')

])
parser= StrOutputParser()
chain= prompt |model | parser


add_routes(
    app,
    chain,
    path='/rag_chain',
    
)

if __name__=='__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)










































