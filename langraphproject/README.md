# 🦜🔗 LangGraph Project

A modular, production-ready **LangGraph** agent project built with LangChain, Google Gemini, and LangSmith observability.

---

## 📁 Project Structure

```
langraph project/
├── main.py            # Entry point — builds & runs the StateGraph agent
├── requirements.txt   # All Python dependencies
├── pyproject.toml     # Build system & project metadata
└── README.md          # This file
```

---

## 🚀 Features

- ✅ **LangGraph StateGraph** — Multi-node graph with conditional routing
- ✅ **Google Gemini LLM** — Powered by `gemini-1.5-flash`
- ✅ **LangSmith Tracing** — Full observability for every run
- ✅ **TypedDict State** — Strongly typed shared state across nodes
- ✅ **Modular Design** — Easy to extend with tools, memory, and more nodes
- ✅ **dotenv Support** — API keys loaded securely from `.env`

---

## ⚙️ Setup

### 1. Clone / Navigate to project

```bash
cd "langraph project"
```

### 2. Create virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or using `pyproject.toml`:

```bash
pip install -e ".[all]"
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
OPENAI_API_KEY=your_openai_api_key_here      # optional
GROQ_API_KEY=your_groq_api_key_here          # optional
ANTHROPIC_API_KEY=your_anthropic_api_key_here # optional
```

---

## ▶️ Run

```bash
python main.py
```

**Expected output:**

```
==================================================
  LangGraph Agent - Starting...
==================================================

[USER]: What is LangGraph and why is it useful?

[AI]: LangGraph is a library built on top of LangChain...

==================================================
  Done.
==================================================
```

---

## 🧠 How It Works

### State

```python
class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], operator.add]
    next_step: str
```

All nodes read from and write to this shared state dictionary.

### Graph Flow

```
START → llm_node → [router] → END
```

| Node | Purpose |
|------|---------|
| `llm_node` | Calls the LLM with current messages |
| `router` | Reads `next_step` to decide routing |

### Extending the Graph

Add a new node and connect it:

```python
workflow.add_node("my_tool_node", my_tool_function)
workflow.add_edge("llm_node", "my_tool_node")
workflow.add_edge("my_tool_node", END)
```

---

## 📦 Key Dependencies

| Package | Purpose |
|---------|---------|
| `langgraph` | Graph-based agent orchestration |
| `langchain-google-genai` | Google Gemini LLM integration |
| `langsmith` | Observability & tracing |
| `python-dotenv` | Secure env variable loading |
| `pydantic` | Data validation |

---

## 🗺️ Roadmap

- [ ] Add tool nodes (web search, calculator)
- [ ] Add memory (checkpointing with SQLite)
- [ ] Add multi-agent subgraph support
- [ ] Add Streamlit / FastAPI interface

---

## 📄 License

MIT © Mohit Payasi
