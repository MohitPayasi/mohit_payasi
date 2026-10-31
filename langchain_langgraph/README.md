# 🦜🕸️ LangChain & LangGraph Workflows

Welcome to the **LangChain & LangGraph** section of the repository! This directory contains practical implementations of end-to-end LLM applications, modern Document Ingestion pipelines, Vector Embeddings, Vector Stores (FAISS), and RAG chains with Groq & LangGraph checkpointing.

---

## 📌 Direct GitHub Notebook Links

Quickly access individual notebooks and modules:

| Topic / Module | Notebook / File | Description |
| :--- | :--- | :--- |
| **Data Ingestion & Splitting** | [`data_ingestion.ipynb`](./introduction/data_ingestion.ipynb) | Document loaders (PDF, Web, Text, Wiki) & chunking strategies |
| **Embeddings & FAISS** | [`embedding.ipynb`](./introduction/embedding.ipynb) | HuggingFace MiniLM embeddings & FAISS vector search |
| **LangChain Core & Memory** | [`langchain.ipynb`](./introduction/langchain.ipynb) | ChatGroq models & `MemorySaver` thread checkpointing |
| **Section 6: End-to-End RAG Project** | [`project.ipynb`](./section_6/project.ipynb) | Production RAG pipeline with Groq LLM & FAISS retriever |
| **Section 7: LCEL Basics** | [`simple_llm_lcel.ipynb`](./section_7/simple_llm_lcel.ipynb) | Modern LangChain Expression Language (LCEL) & Runnable chains |
| **Dependencies** | [`requirement.txt`](./requirement.txt) | Environment requirements for this section |

---

## 🗂️ Directory Structure

```text
langchain_langgraph/
├── introduction/
│   ├── data_ingestion.ipynb      # TextLoader, PyPDFLoader, WebBaseLoader, WikipediaLoader & Text Splitters
│   ├── embedding.ipynb           # HuggingFace Embeddings, SentenceTransformer & FAISS Vector Indexing
│   ├── langchain.ipynb           # ChatGroq, Message types & LangGraph MemorySaver checkpointing
│   └── faiss_index/              # Serialized FAISS index files (index.faiss, index.pkl)
│
├── section_6/
│   ├── project.ipynb             # Complete End-to-End RAG Chain with Groq LLM & FAISS Retrieval
│   └── faiss_index/              # Project specific persistent FAISS vector store
│
├── section_7/
│   └── simple_llm_lcel.ipynb     # Declarative pipelines with LangChain Expression Language (LCEL)
│
├── requirement.txt               # All required dependencies
└── README.md                     # Section documentation
```

---

## 🚀 Detailed Module Breakdown

### 1. `introduction/data_ingestion.ipynb`
- **Document Loaders**:
  - `TextLoader`: Local `.txt` files parsing.
  - `PyPDFLoader`: PDF documents parsing and page extraction.
  - `WebBaseLoader`: Web scraping and converting web content into LangChain Documents.
  - `WikipediaLoader`: Direct Wikipedia querying and document construction.
- **Text Splitting**:
  - `CharacterTextSplitter` & `RecursiveCharacterTextSplitter` with tuned `chunk_size` and `chunk_overlap`.

### 2. `introduction/embedding.ipynb`
- **Embeddings**:
  - HuggingFace open-source sentence-transformer embeddings (`sentence-transformers/all-MiniLM-L6-v2`).
- **Vector Storage**:
  - **FAISS** (Facebook AI Similarity Search) dense vector indexing and local disk persistence.
- **Retriever Interface**:
  - LangChain `as_retriever()` for semantic vector search queries.

### 3. `introduction/langchain.ipynb`
- **ChatGroq Integration**: Fast inference with models like `mixtral-8x7b-32768` and `llama-3.3-70b-versatile`.
- **LangGraph Checkpointing**: State persistence and thread management with `MemorySaver`.

### 4. `section_6/project.ipynb` (End-to-End RAG Project)
- **Production RAG Architecture**:
  - Question Answering system combining `ChatGroq`, `ChatPromptTemplate`, `FAISS`, and `StrOutputParser`.
  - Dynamic context passing through retrieved vector chunks.

### 5. `section_7/simple_llm_lcel.ipynb` (LCEL)
- **LangChain Expression Language**:
  - Pipe operator syntax (`prompt | model | parser`).
  - Standard `Runnable` methods: `invoke()`, `batch()`, `stream()`.
  - Streamlined pipeline composition without legacy chain overhead.

---

## ⚙️ Quick Start

```bash
cd langchain_langgraph
pip install -r requirement.txt
```
