# 🧠 AI Engineering & LLM Systems: LangChain, LangGraph & Machine Learning

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/🦜🔗_LangChain-0.3+-darkgreen.svg)](https://python.langchain.com/)
[![LangGraph](https://img.shields.io/badge/🕸️_LangGraph-StateGraph-orange.svg)](https://langchain-ai.github.io/langgraph/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-teal.svg)](https://fastapi.tiangolo.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A modular, hands-on repository containing production-grade architectures, agentic workflows, declarative LCEL pipelines, RAG systems, and fundamental Machine Learning algorithms.

---

## 📑 Table of Contents

- [🗂️ Repository Architecture](#️-repository-architecture)
- [🧩 Modules Overview](#-modules-overview)
  - [1. LangChain Fundamentals (`1-langchain_basic/`)](#1-langchain-fundamentals-1-langchain_basic)
  - [2. End-to-End RAG & LCEL (`langchain_langgraph/`)](#2-end-to-end-rag--lcel-langchain_langgraph)
  - [3. Agentic Systems with LangGraph (`langraphproject/`)](#3-agentic-systems-with-langgraph-langraphproject)
  - [4. Advanced LangChain Features (`project/`)](#4-advanced-langchain-features-project)
  - [5. API Serving & Deployment (`practice/`)](#5-api-serving--deployment-practice)
  - [6. Machine Learning Foundations (`Machine_learning/`)](#6-machine-learning-foundations-machine_learning)
- [⚡ Quick Start & Setup](#-quick-start--setup)
- [🔑 Environment Variables](#-environment-variables)
- [🛠️ Tech Stack](#️-tech-stack)
- [👤 Author](#-author)

---

## 🗂️ Repository Architecture

```text
mohit_payasi/
├── 1-langchain_basic/          # Fundamentals: Ingestion, Chunking, Embeddings & Vector DBs
│   ├── 1.1open_ai/             # Chroma, FAISS, OpenAI & HuggingFace Embeddings
│   ├── 1.2ollama/              # Local LLMs & Embeddings via Ollama
│   └── README.md
│
├── langchain_langgraph/        # End-to-End RAG, Embeddings, Ingestion & LCEL
│   ├── introduction/           # Document Ingestion, HF Embeddings & LangGraph Memory
│   ├── section_6/              # Production RAG pipeline with Groq LLM & FAISS
│   ├── section_7/              # Declarative LCEL (LangChain Expression Language) Chains
│   └── README.md
│
├── langraphproject/            # Production Agent Systems built with LangGraph
│   ├── basic_chat/             # StateGraph Nodes, Edges, State & LangSmith Observability
│   ├── main.py                 # Standalone StateGraph Agent with Gemini & LangSmith
│   └── README.md
│
├── project/                    # Advanced LangChain Core Features
│   ├── project_1/              # Core Blocks: Tools, Middleware, Structured Output, Streaming
│   └── README.md
│
├── practice/                   # Deployment, Web APIs & Serving
│   ├── chat_bot.py             # FastAPI + LangServe API server for LCEL chains
│   ├── fast_api.py             # FastAPI service with Windows UTF-8 banner fix
│   ├── chatbot.ipynb           # Interactive prompt & model testing
│   └── README.md
│
├── Machine_learning/           # Fundamental ML & Data Science Notebooks
│   ├── class_2.ipynb           # Descriptive Statistics & Data Summaries
│   ├── class_3.ipynb           # Exploratory Data Analysis (EDA) & Seaborn
│   ├── class_4.ipynb           # Feature Engineering & Categorical Encoding
│   ├── class_5.ipynb           # Outlier Detection, Boxplots & Z-Score Analysis
│   ├── class_6.ipynb           # Simple Linear Regression
│   ├── class_7.ipynb           # Multiple Linear Regression & Error Metrics
│   └── README.md
│
├── scripts/                    # Automation & developer utility scripts
│   └── auto_commit.ps1         # Periodic sync utility
│
├── .env.example                # Template for LLM and Observability credentials
├── pyproject.toml              # Unified package configuration
├── requirements.txt            # Project dependencies
└── README.md                   # Repository overview
```

---

## 🧩 Modules Overview

### 1. LangChain Fundamentals (`1-langchain_basic/`)
* **Document Loaders**: `PyPDFLoader`, `TextLoader`, `WebBaseLoader` for unstructured data parsing.
* **Text Chunking**: Comparisons between `CharacterTextSplitter` and `RecursiveCharacterTextSplitter`.
* **Embedding Providers**: OpenAI (`text-embedding-3-small`) and open-source HuggingFace models (`sentence-transformers/all-MiniLM-L6-v2`).
* **Vector Stores**: Dense semantic indexing and search using **FAISS** and **ChromaDB**.

### 2. End-to-End RAG & LCEL (`langchain_langgraph/`)
* **RAG Pipeline (Section 6)**: Production Question-Answering system connecting Groq LLM, FAISS retriever, and structured prompt templates.
* **Modern LCEL (Section 7)**: Declarative pipeline construction with Unix-style pipe syntax (`prompt | model | parser`), supporting streaming, batching, and async operations.
* **State Checkpointing**: Thread management using `langgraph.checkpoint.memory.MemorySaver`.
* 👉 Check out [`langchain_langgraph/README.md`](./langchain_langgraph/README.md) for full module documentation.

### 3. Agentic Systems with LangGraph (`langraphproject/`)
* **StateGraph Architecture**: Cyclic graphs with shared `TypedDict` state schemas.
* **Routing**: Dynamic branch execution using conditional edges and function tools.
* **Model Dynamic Initialization**: Provider switching with `init_chat_model()`.
* **Observability**: Production monitoring, latency tracing, and token tracking with **LangSmith**.

### 4. Advanced LangChain Features (`project/`)
* **Structured Output**: Extracting schema-validated JSON directly into Pydantic models with `.with_structured_output()`.
* **Custom Tools**: Equipping agents with external execution capabilities via `@tool` decorators.
* **Lifecycle Callbacks**: Custom middleware handlers (`BaseCallbackHandler`) intercepting `on_llm_start`, `on_llm_end`, and `on_llm_error`.

### 5. API Serving & Deployment (`practice/`)
* **FastAPI + LangServe**: Exposing LCEL chains as production REST endpoints with automated OpenAPI docs and interactive web playgrounds (`/rag_chain/playground`).
* **Platform Hardening**: Windows UTF-8 command-line encoding resolutions for seamless server boots.

### 6. Machine Learning Foundations (`Machine_learning/`)
* **Statistics & EDA**: Univariate/multivariate analysis, correlation matrices, and distribution analysis with Pandas and Seaborn.
* **Data Preparation**: Label encoding, one-hot encoding, and outlier filtering using IQR and Z-scores.
* **Regression Modeling**: Simple and Multiple Linear Regression implementations from scratch and using Scikit-Learn.
* 👉 Check out [`Machine_learning/README.md`](./Machine_learning/README.md) for full syllabus breakdown.

---

## ⚡ Quick Start & Setup

### 1. Clone Repository
```bash
git clone https://github.com/MohitPayasi/mohit_payasi.git
cd mohit_payasi
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Copy the provided [`.env.example`](./.env.example) to `.env` and configure your API credentials:

```bash
cp .env.example .env
```

Key variables required:
```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_gemini_key
OPENAI_API_KEY=your_openai_api_key
HF_TOKEN=your_huggingface_token
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
```

---

## 🛠️ Tech Stack

| Category | Technologies |
| :--- | :--- |
| **LLM Orchestration** | LangChain, LangGraph, LCEL, LangServe |
| **Model Providers** | Groq (Llama 3, Mixtral), Google Gemini, OpenAI, Ollama |
| **Embeddings & Vector Stores** | HuggingFace Sentence Transformers, FAISS, ChromaDB |
| **Backend & Serving** | FastAPI, Uvicorn, Pydantic |
| **Data Science & ML** | Scikit-Learn, NumPy, Pandas, Matplotlib, Seaborn, SciPy |
| **Monitoring & Tracing** | LangSmith |

---

## 👤 Author

**Mohit Payasi**
* GitHub: [@MohitPayasi](https://github.com/MohitPayasi)
* Repository: [mohit_payasi](https://github.com/MohitPayasi/mohit_payasi)
