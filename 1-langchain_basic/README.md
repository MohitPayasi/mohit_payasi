# 📚 1-LangChain Basic: RAG & Data Pipelines

This module covers the foundational building blocks of **Retrieval-Augmented Generation (RAG)** systems using **LangChain**. It focuses on data extraction, text chunking, embedding generation, vector stores, and retrieval techniques.

---

## 📂 Subdirectories

- **[`1.1open_ai/`](./1.1open_ai/)** — Comprehensive notebooks for document ingestion, text splitting, OpenAI & HuggingFace embeddings, and Chroma & FAISS vector databases.
- **[`1.2ollama/`](./1.2ollama/)** — Local model orchestration, offline embeddings, and local inference pipelines.

---

## 🛠️ Key Topics Implemented

1. **Document Ingestion (`data_ingestion.ipynb`)**:
   - Ingesting text files (`TextLoader`), PDF documents (`PyPDFLoader`), and web pages (`WebBaseLoader`).
   - Extracting raw text and preserving metadata.

2. **Text Splitting & Chunking (`data_spitter.ipynb`)**:
   - Understanding why chunking is required (context length limitations and retrieval relevance).
   - Comparing fixed-size splitting (`CharacterTextSplitter`) with structure-aware splitting (`RecursiveCharacterTextSplitter`).
   - Setting `chunk_size` and `chunk_overlap` effectively.

3. **Embeddings (`open_ai_embedding.ipynb` & `hugging_face_embedding.ipynb`)**:
   - Converting text chunks into high-dimensional dense vectors.
   - Using proprietary embeddings (OpenAI `text-embedding-3-small` / `ada-002`).
   - Using open-source local embeddings (HuggingFace `sentence-transformers/all-MiniLM-L6-v2`).

4. **Vector Databases (`croma_vector_db.ipynb` & `faiss_vector_db.ipynb`)**:
   - Creating local persistent vector stores with **ChromaDB**.
   - In-memory similarity search and indexing with **FAISS** (Facebook AI Similarity Search).
   - Executing top-k semantic similarity queries (`similarity_search`, `similarity_search_with_score`).

---

## 📦 Requirements & Installation

Dependencies are listed in [`requirement.txt`](./requirement.txt):

```bash
pip install -r requirement.txt
```

Key packages:
- `langchain`
- `langchain-community`
- `langchain-openai`
- `langchain-huggingface`
- `chromadb`
- `faiss-cpu`
- `pypdf`
