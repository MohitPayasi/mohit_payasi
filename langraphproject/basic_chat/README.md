# 💬 LangGraph Basic Chat & Monitoring

This directory contains practical Jupyter Notebooks demonstrating stateful, graph-based agents built with **LangGraph**, dynamic model initialization, and end-to-end observability via **LangSmith**.

---

## 📓 Notebooks & What Was Done

### 1. `basic_chat_1.ipynb` — LangGraph Fundamentals
- **Core Concepts Covered**:
  - **State**: Defined a strongly-typed shared state schema using Python's `typing.TypedDict`.
  - **Nodes**: Implemented standalone computational functions (nodes) that read from and update the graph state.
  - **Edges**: Added standard directional edges connecting nodes, as well as `START` and `END` control nodes.
  - **Graph Compilation**: Compiled the `StateGraph` into an executable runnable using `.compile()`.
  - **Chat Node Implementation**: Connected a ChatGroq LLM inside a node to generate conversational responses.

### 2. `debug_monitoring.ipynb` — Model Initialization & Observability
- **Core Concepts Covered**:
  - **Unified Model Initialization**:
    ```python
    from langchain.chat_models import init_chat_model
    model1 = init_chat_model(model='openai/gpt-oss-20b', model_provider='groq')
    ```
    Used `init_chat_model` to decouple the application code from specific provider client classes.
  - **Response Metadata Inspection**: Extracted token usage (`usage_metadata`) and execution latency from model responses.
  - **Lifecycle Callbacks (`MonitoringCallbackHandler`)**: Built custom `BaseCallbackHandler` implementing `on_llm_start`, `on_llm_end`, and `on_llm_error` for client-side logging and debugging.
  - **Tool Calling & ToolNode**: Built a self-routing agent workflow using `@tool`, `bind_tools`, `ToolNode`, and `tools_condition` with message state reducer (`add_messages`).

### 3. `multiaiagent.ipynb` — Multi-Agent Architecture
- Multi-agent orchestration, collaboration, and role specialization in LangGraph.

---

## 🔑 Environment Setup (`.env`)

Ensure the following variables are configured in `.env`:

```env
GROQ_API_KEY=your_groq_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=your_project_name
```
