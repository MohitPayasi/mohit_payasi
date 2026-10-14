# 🔍 1.1 OpenAI & RAG Core Pipelines

This directory contains complete step-by-step Jupyter Notebooks demonstrating the core stages of building a **Retrieval-Augmented Generation (RAG)** pipeline.

---

## 📓 Notebooks & Implementation Details

| Notebook | Purpose & What Was Done |
| :--- | :--- |
| **`data_ingestion.ipynb`** | Loaded data from diverse sources including raw text (`speech.txt`), JSON data (`speech.json`), PDF files (`XYZ.pdf`), and web URLs using LangChain loaders (`TextLoader`, `PyPDFLoader`, `WebBaseLoader`). |
| **`data_spitter.ipynb`** | Demonstrated text chunking strategies. Implemented `CharacterTextSplitter` and `RecursiveCharacterTextSplitter` with customizable `chunk_size` and `chunk_overlap` to maintain context across chunk boundaries. |
| **`open_ai_embedding.ipynb`** | Utilized OpenAI's embedding API (`OpenAIEmbeddings`) to convert chunks into dense vector representations. Verified dimensionality and vector norms. |
| **`hugging_face_embedding.ipynb`** | Implemented open-source embeddings using `HuggingFaceEmbeddings` with models such as `sentence-transformers/all-MiniLM-L6-v2` for offline/cost-free vectorization. |
| **`croma_vector_db.ipynb`** | Initialized a persistent **ChromaDB** collection, inserted embedded document chunks, persisted the database locally to `./croma_db`, and executed semantic similarity search queries. |
| **`faiss_vector_db.ipynb`** | Built a high-performance vector index using **FAISS** (`faiss-cpu`), performed nearest-neighbor similarity searches, and saved/loaded the FAISS index to disk. |

---

## 📄 Sample Data Files

- **`speech.txt`**: Sample long-form speech text used for testing text loaders and chunking algorithms.
- **`speech.json`**: Structured JSON document used for testing structured data ingestion.
- **`XYZ.pdf`**: Sample PDF document used to test PDF extraction and page-by-page metadata handling.

---

## 🔑 Environment Configuration

Create a `.env` file inside this directory or the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
HF_TOKEN=your_huggingface_token
```
