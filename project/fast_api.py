import sys
import io
import os

# Fix Windows console encoding for LangServe ASCII banner (UnicodeEncodeError '\u2502')
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
from langserve import add_routes
# Load environment variables
load_dotenv()
groq_api = os.getenv("GROQ_API")

# Initialize ChatGroq model
model = ChatGroq(model="openai/gpt-oss-20b", api_key=groq_api)

system_prompt = "you are ai agent perform given task"

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{question}")
])

output = StrOutputParser()

rag_chain = prompt | model | output

# FastAPI App
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="simple llm model"
)

# LangServe routes
add_routes(app, rag_chain, path="/rag_chain")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
