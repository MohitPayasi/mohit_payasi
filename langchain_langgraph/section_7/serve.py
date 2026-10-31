
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY']= os.getenv('GROQ_API_KEY')

app= FastAPI(title= 'Langchain serve '
,description='this is basic project')



from langchain_groq import ChatGroq

llm=ChatGroq(model='openai/gpt-oss-20b')

generic_template= 'translate the following into {langauge}'

prompt= ChatPromptTemplate.from_messages([
    ('system', generic_template),('user',"{text}")])

str= StrOutputParser()

chain= prompt|llm|str

# app definition


add_routes(
app,chain,path='/chain'
)
if __name__=='__main__':
    import uvicorn
    uvicorn.run(app,host='localhost',port=8000)




















