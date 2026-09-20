"""
Run this script once to populate gettingstarted.ipynb with all LangChain cells.
Usage:  python update_notebook.py
"""
import json, os

nb = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# LangChain + OpenAI — Getting Started\n",
    "Core building blocks: environment, ChatOpenAI, prompts, LCEL chains, streaming, memory."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "print('Python path:', sys.executable)\n",
    "print('Python version:', sys.version)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "import langchain\n",
    "print('LangChain version:', langchain.__version__)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 1. Load Environment Variables"]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "from dotenv import load_dotenv\n",
    "import os\n",
    "\n",
    "# Load .env from parent directory (1-langchain/.env)\n",
    "load_dotenv(dotenv_path='../.env')\n",
    "\n",
    "print('Environment loaded!')\n",
    "print('OpenAI Key set  :', bool(os.getenv('OPENAI_API_KEY')))\n",
    "print('LangChain Key set:', bool(os.getenv('LANGCHAIN_API_KEY')))\n",
    "print('Tracing enabled :', os.getenv('LANGCHAIN_TRACING_V2'))\n",
    "print('Project         :', os.getenv('LANGCHAIN_PROJECT'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 2. Basic Chat — ChatOpenAI"]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain_openai import ChatOpenAI\n",
    "\n",
    "# Initialize the model (gpt-4o-mini is cheap & fast)\n",
    "llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.7)\n",
    "\n",
    "response = llm.invoke('What is LangChain in one sentence?')\n",
    "print(response.content)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 3. Prompt Templates"]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain_core.prompts import ChatPromptTemplate\n",
    "\n",
    "prompt = ChatPromptTemplate.from_messages([\n",
    "    ('system', 'You are a helpful assistant that explains {topic} concepts simply.'),\n",
    "    ('human', '{question}')\n",
    "])\n",
    "\n",
    "formatted = prompt.format_messages(\n",
    "    topic='machine learning',\n",
    "    question='What is a neural network?'\n",
    ")\n",
    "for msg in formatted:\n",
    "    print(f'[{msg.type.upper()}]: {msg.content}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 4. LCEL Chain — prompt | llm | parser"]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain_core.output_parsers import StrOutputParser\n",
    "\n",
    "# Build the chain using pipe operator\n",
    "chain = prompt | llm | StrOutputParser()\n",
    "\n",
    "result = chain.invoke({\n",
    "    'topic': 'machine learning',\n",
    "    'question': 'What is a neural network?'\n",
    "})\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 5. Streaming Responses"]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Tokens stream in as they are generated\n",
    "for chunk in chain.stream({\n",
    "    'topic': 'Python programming',\n",
    "    'question': 'Explain list comprehensions with an example.'\n",
    "}):\n",
    "    print(chunk, end='', flush=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": ["## 6. Conversational Memory — Message History"]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain_core.messages import HumanMessage, SystemMessage, AIMessage\n",
    "\n",
    "# Pass full conversation history so the model has context\n",
    "messages = [\n",
    "    SystemMessage(content='You are a concise and friendly AI assistant.'),\n",
    "    HumanMessage(content='Hi! My name is Mohit.'),\n",
    "    AIMessage(content='Hi Mohit! How can I help you today?'),\n",
    "    HumanMessage(content='What was my name again?')\n",
    "]\n",
    "\n",
    "response = llm.invoke(messages)\n",
    "print(response.content)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (langchain-env)",
   "language": "python",
   "name": "langchain-env"
  },
  "language_info": {
   "name": "python",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

out = r"d:\mohit_payasi\langchain\1-langchain\1.1open_ai\gettingstarted.ipynb"
with open(out, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print(f"✅ Notebook written to: {out}")
