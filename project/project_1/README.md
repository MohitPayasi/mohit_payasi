# 🛠️ Project 1: Advanced LangChain Building Blocks

This directory contains deep-dive implementations of core LangChain paradigms, from LCEL and message flows to middleware, streaming, structured outputs, and agent tools.

---

## 📓 Notebooks & Implementation Details

| Notebook / Document | Purpose & What Was Done |
| :--- | :--- |
| **`langchain_v1.ipynb`** | Explored LangChain core concepts and LCEL syntax. Built declarative chains connecting prompts, models, and output parsers using the `\|` pipe operator. |
| **`messages.ipynb`** | Detailed study of LangChain message classes (`HumanMessage`, `AIMessage`, `SystemMessage`, `ToolMessage`). Handled conversational turns and multi-message contexts. |
| **`middle_ware.ipynb`** & **`middleware_notes.md`** | Implemented custom middleware behavior using `BaseCallbackHandler`. Intercepted execution lifecycle events (`on_llm_start`, `on_llm_end`, `on_llm_error`, `on_chain_start`, `on_chain_end`) for logging, latency measurement, and error handling. |
| **`model_integration.ipynb`** | Integrated multiple model backends across different providers (Groq, OpenAI, Google Gemini) to compare latency, quality, and API compatibility. |
| **`streaming_batch.ipynb`** | Explored high-performance inference mechanisms: implemented token-by-token real-time streaming using `.stream()` and parallel batch execution using `.batch()`. |
| **`structureoutput.ipynb`** | Enforced structured model output using Pydantic schemas and `.with_structured_output(...)`. Extracted validated JSON schemas directly from unstructured natural language inputs. |
| **`tools_creation.ipynb`** | Built custom agent tools using the `@tool` decorator. Configured docstrings and type annotations to generate tool schemas, bound tools to models, and handled tool call outputs. |

---

## 🖼️ Media & Architecture References

- **`langchain_tools_theory.jpg`** — Visual diagram illustrating the interaction loop: `User → LLM → Tool Call → Tool Execution → Result → LLM → Final Response`.

---

## 🔑 Environment Configuration

Ensure your `.env` contains:
```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
```
