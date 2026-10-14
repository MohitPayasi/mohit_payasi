# ⚡ Practice: FastAPI & LangServe Deployment

This folder contains implementations focused on deploying LangChain pipelines as production-ready web APIs using **FastAPI** and **LangServe**, along with interactive notebooks for rapid experimentation.

---

## 📂 Files & What Was Done

### 1. `chat_bot.py`
- Built a **FastAPI** application integrated with **LangServe**.
- Configured a LCEL chain:
  ```python
  prompt = ChatPromptTemplate.from_messages([
      ('system', 'You are {domain_name} content creator'),
      ('user', '{question}')
  ])
  parser = StrOutputParser()
  chain = prompt | model | parser
  ```
- Exposed the chain using LangServe's `add_routes(app, chain, path='/rag_chain')` providing automatic REST API endpoints, streaming, and a built-in web playground at `/rag_chain/playground`.

### 2. `fast_api.py`
- Fixed a known Windows console issue where LangServe's ASCII banner triggers `UnicodeEncodeError` (character `\u2502`) by wrapping `sys.stdout` and `sys.stderr` with UTF-8 encoding:
  ```python
  if sys.platform == "win32":
      sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
      sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
  ```
- Deployed a robust ChatGroq agent service running with Uvicorn on `http://127.0.0.1:8000`.

### 3. `chatbot.ipynb`
- Interactive Jupyter Notebook testing different prompt variations, system roles, and model outputs using Groq's high-speed inference.

### 4. `test.ipynb`
- Scratchpad notebook for validating components, testing parser behaviors, and debugging API connections.

---

## ▶️ Running the Server

```bash
python fast_api.py
```
Open your browser to:
- API Documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Interactive Playground: [http://127.0.0.1:8000/rag_chain/playground](http://127.0.0.1:8000/rag_chain/playground)
