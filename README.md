# 🦜🔗 LangChain & LangGraph Mastery Repository

Welcome to the **LangChain & LangGraph** learning and development repository by **Mohit Payasi**. This repository contains hands-on implementations, end-to-end architectures, experiments, and production-ready code covering the entire modern LLM application development lifecycle.

---

## 🗂️ Repository Structure Overview

```text
langchain/
├── 1-langchain_basic/          # Fundamentals: Ingestion, Text Splitting, Embeddings & Vector DBs
│   ├── 1.1open_ai/             # Chroma, FAISS, OpenAI & HuggingFace Embeddings, Document Loaders
│   └── 1.2ollama/              # Local LLMs & Embeddings via Ollama
│
├── langchain_langgraph/        # End-to-End RAG, Embeddings, Ingestion & LangGraph Checkpointing
│   ├── introduction/           # Document Ingestion, HF Embeddings & LangGraph Memory
│   ├── section_6/              # End-to-End Project with Groq LLM & FAISS
│   └── README.md               # Dedicated documentation with direct notebook links
│
├── langraphproject/            # Production Agent Systems built with LangGraph
│   ├── main.py                 # Standalone StateGraph Agent with Google Gemini & LangSmith
│   └── basic_chat/             # LangGraph Nodes, Edges, State & LangSmith Tracing/Monitoring
│
├── practice/                   # Deployment, Web APIs & Serving
│   ├── chat_bot.py             # FastAPI + LangServe API server for LCEL chains
│   ├── fast_api.py             # FastAPI service with Windows UTF-8 banner fix
│   ├── chatbot.ipynb           # Interactive prompt & model testing
│   └── test.ipynb              # Component tests
│
└── project/                    # Advanced LangChain Core Features
    ├── chatbot.ipynb           # Chat model comparisons & message schema experiments
    ├── cloud_env.bat           # Environment configuration script
    └── project_1/              # Core building blocks: LCEL, Tools, Middleware, Structured Output
        ├── langchain_v1.ipynb  # LangChain core syntax & chain composition
        ├── messages.ipynb      # Message roles (Human, AI, System, Tool)
        ├── middle_ware.ipynb   # Lifecycle callbacks & middleware interception
        ├── middleware_notes.md # Deep dive into LangChain callback architecture
        ├── model_integration.ipynb # Multi-provider setups (Groq, OpenAI, Google)
        ├── streaming_batch.ipynb   # Streaming responses (.stream) & batch processing (.batch)
        ├── structureoutput.ipynb   # Typed schemas with Pydantic & with_structured_output
        └── tools_creation.ipynb    # Custom tool definitions (@tool) & function calling
```

---

## 🚀 Key Modules & What Has Been Done

### 1. `1-langchain_basic/`
- **Data Ingestion**: Loading PDFs, text documents, and web pages via LangChain Document Loaders (`PyPDFLoader`, `TextLoader`, `WebBaseLoader`).
- **Text Chunking**: Chunking strategy comparisons using `CharacterTextSplitter` and `RecursiveCharacterTextSplitter`.
- **Embeddings**: Vector embeddings generation using OpenAI (`text-embedding-3-small`) and HuggingFace (`sentence-transformers/all-MiniLM-L6-v2`).
- **Vector Databases**: Semantic search indexing and query retrieval using **Chroma** and **FAISS**.

### 2. `langchain_langgraph/`
- **Comprehensive Guide & Links**: Check out [`langchain_langgraph/README.md`](./langchain_langgraph/README.md) for direct notebook access.
- **Data Ingestion & Splitting**: PDF, text, web scraping (`WebBaseLoader`), and Wikipedia loading coupled with recursive character text chunking.
- **Embeddings & FAISS**: Open-source HuggingFace Sentence Transformers with local FAISS persistence and vector similarity retrieval.
- **LangGraph Checkpointing & Groq**: Chat Groq setup with `langgraph.checkpoint.memory.MemorySaver` thread configurations.
- **End-to-End RAG Project (Section 6)**: Production RAG pipeline chaining Groq LLM, FAISS retriever, ChatPromptTemplate, and StrOutputParser.

### 3. `langraphproject/`
- **LangGraph StateGraph**: Cyclic and stateful agent architecture using `TypedDict` for shared state management.
- **Node & Edge Routing**: Connecting graph nodes via direct edges and conditional edges.
- **Dynamic Model Initialization**: Model provider switching with `init_chat_model(model='openai/gpt-oss-20b', model_provider='groq')`.
- **Observability**: Full tracing, latency monitoring, and token debugging using **LangSmith**.

### 4. `practice/`
- **FastAPI & LangServe**: Exposing LangChain chains as RESTful endpoints with automatic OpenAPI documentation and interactive playground (`/rag_chain/playground`).
- **Encoding & Compatibility**: Handling Windows UTF-8 encoding issues gracefully during server boot.

### 5. `project/` & `project/project_1/`
- **LCEL Composition**: Creating declarative pipelines using the pipe operator (`prompt | model | parser`).
- **Structured Output**: Extracting structured data directly into Pydantic models.
- **Tool Calling**: Equipping models with external tools via `@tool` decorators.
- **Middleware & Callbacks**: Implementing `BaseCallbackHandler` to intercept execution hooks (`on_llm_start`, `on_llm_end`, `on_llm_error`).

---

## ⚙️ Quick Start

### 1. Clone & Setup Environment
```bash
# Clone the repository
git clone https://github.com/MohitPayasi/mohit_payasi.git
cd mohit_payasi

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate # On Linux/macOS
```

### 2. Install Dependencies
```bash
pip install -r 1-langchain_basic/requirement.txt
# or for langgraph project
pip install -r langraphproject/requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the relevant folder with your credentials:
```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=your_project_name
```

---

## 👤 Author
- **Mohit Payasi**
- GitHub: [@MohitPayasi](https://github.com/MohitPayasi)
