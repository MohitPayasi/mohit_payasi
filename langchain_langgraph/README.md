# 🦜🕸️ LangChain & LangGraph Workflows

Welcome to the **LangChain & LangGraph** section of the repository! This directory contains practical implementations of end-to-end LLM applications, modern Document Ingestion pipelines, Vector Embeddings, Vector Stores (FAISS), and RAG chains with Groq & LangGraph checkpointing.

---

## 📌 Direct GitHub Notebook Links

Agar aap GitHub par direct kisi bhi notebook ya folder ko access karna chahte hain, toh neeche diye gaye direct links use kar sakte hain:

| Topic / Module | Notebook / File | Direct GitHub Link |
| :--- | :--- | :--- |
| **Data Ingestion & Splitting** | `data._ingestion.ipynb` | [Open Ingestion Notebook](https://github.com/MohitPayasi/mohit_payasi/blob/main/langchain_langgraph/introduction/data._ingestion.ipynb) |
| **Embeddings & FAISS Retriever** | `embedding.ipynb` | [Open Embedding Notebook](https://github.com/MohitPayasi/mohit_payasi/blob/main/langchain_langgraph/introduction/embedding.ipynb) |
| **LangChain Core & Memory** | `langchain.ipynb` | [Open LangChain Notebook](https://github.com/MohitPayasi/mohit_payasi/blob/main/langchain_langgraph/introduction/langchain.ipynb) |
| **Section 6: End-to-End RAG Project** | `project.ipynb` | [Open Section 6 Project](https://github.com/MohitPayasi/mohit_payasi/blob/main/langchain_langgraph/section_6/project.ipynb) |
| **Environment Dependencies** | `requirement.txt` | [View Requirements](https://github.com/MohitPayasi/mohit_payasi/blob/main/langchain_langgraph/requirement.txt) |

---

## 🗂️ Directory Structure

```text
langchain_langgraph/
├── introduction/
│   ├── data._ingestion.ipynb     # TextLoader, PyPDFLoader, WebBaseLoader, WikipediaLoader & Text Splitters
│   ├── embedding.ipynb           # HuggingFace Embeddings, SentenceTransformer & FAISS Vector Indexing
│   ├── langchain.ipynb           # ChatGroq, Message types & LangGraph MemorySaver checkpointing
│   └── faiss_index/              # Serialized FAISS index files (index.faiss, index.pkl)
│
├── section_6/
│   ├── project.ipynb             # Complete End-to-End RAG Chain with Groq LLM & FAISS Retrieval
│   └── faiss_index/              # Project specific persistent FAISS vector store
│
├── requirement.txt               # All required dependencies
├── .env.example                  # Template for API keys
└── README.md                     # Documentation with direct links
```

---

## 🚀 Detailed Module Breakdown

### 1. `introduction/data._ingestion.ipynb`
- **Document Loaders**:
  - `TextLoader`: Local `.txt` files load karne ke liye.
  - `PyPDFLoader`: PDF documents ko extract aur parse karne ke liye.
  - `WebBaseLoader`: Web pages se content scrape karke document create karne ke liye.
  - `WikipediaLoader`: Wikipedia topics se seedha information load karne ke liye.
- **Text Splitting**:
  - `CharacterTextSplitter` aur `RecursiveCharacterTextSplitter` ka use karke documents ko meaningful chunks me divide karna with `chunk_size` aur `chunk_overlap`.

### 2. `introduction/embedding.ipynb`
- **Embeddings**:
  - HuggingFace open-source sentence-transformer embeddings (`sentence-transformers/all-MiniLM-L6-v2`) ka integration.
- **Vector Storage**:
  - **FAISS** (Facebook AI Similarity Search) ke sath dense vectors ko index aur locally persist (`faiss_index/`) karna.
- **Retriever Interface**:
  - LangChain `as_retriever()` interface ke through semantic search queries run karna.

### 3. `introduction/langchain.ipynb`
- **Groq Integration**:
  - Ultra-fast inference with `ChatGroq`.
- **Core Message Schema**:
  - `HumanMessage`, `AIMessage`, aur `SystemMessage` ke structured conversation flows.
- **State Checkpointing**:
  - `langgraph.checkpoint.memory.MemorySaver` ka use karke thread-based conversation memory configure karna (`thread_id`).

### 4. `section_6/project.ipynb`
- **End-to-End RAG Pipeline**:
  - Groq LLM (`ChatGroq`) ke sath ChatPromptTemplate, FAISS Retriever, aur `StrOutputParser` ko LCEL (`|`) pipe operator ke through ek unified chain me tie karna.

---

## ⚙️ How to Setup & Run

### 1. Virtual Environment Setup
```bash
# langchain_langgraph folder ke andar jayein
cd langchain_langgraph

# Virtual environment banayein
python -m venv .venv

# Environment activate karein (Windows PowerShell)
.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
```bash
pip install -r requirement.txt
```

### 3. Environment Variables
Folder ke andar `.env` file banayein aur apni API keys daalein:
```env
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_TRACING_V2=true
```

---

## 🔗 Repository Navigation
- 🏠 [Root Repository Overview](https://github.com/MohitPayasi/mohit_payasi)
- 📚 [LangChain Basics](../1-langchain_basic/README.md)
- 🤖 [LangGraph Project](../langraphproject/README.md)

