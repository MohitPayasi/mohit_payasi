# 🦙 1.2 Ollama: Local LLM & Local Embeddings

This directory is dedicated to running **local, privacy-focused open-source language models** and embeddings using **Ollama** integrated with LangChain.

---

## 🎯 Objectives & What Was Done

- **Local Inference**: Connecting LangChain to a locally hosted Ollama instance (`http://localhost:11434`) without relying on cloud API keys.
- **Models**: Running open-weight models such as:
  - `llama3`, `llama3.2`
  - `mistral`
  - `nomic-embed-text` (for local embeddings)
- **Local RAG Integration**: Generating embeddings locally and indexing them in local vector databases (Chroma / FAISS) for a 100% offline RAG architecture.

---

## 🚀 Getting Started with Ollama

1. Install Ollama from [ollama.com](https://ollama.com/).
2. Pull required models in your terminal:
   ```bash
   ollama run llama3
   ollama pull nomic-embed-text
   ```
3. Usage in LangChain:
   ```python
   from langchain_community.llms import Ollama
   from langchain_community.embeddings import OllamaEmbeddings

   llm = Ollama(model="llama3")
   embeddings = OllamaEmbeddings(model="nomic-embed-text")
   ```
