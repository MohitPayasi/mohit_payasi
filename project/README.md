# 🚀 Project: Advanced LangChain Concepts & Implementations

This module serves as the primary workspace for advanced LangChain techniques, including chain composition, message schemas, custom middleware, structured output, and tool calling.

---

## 📂 Subdirectories & Files

- **[`project_1/`](./project_1/)** — Comprehensive collection of notebooks demonstrating core LangChain v1/v2 features:
  - LCEL (LangChain Expression Language)
  - Message handling (`HumanMessage`, `AIMessage`, `SystemMessage`)
  - Middleware & Callbacks (`BaseCallbackHandler`)
  - Multi-provider model integrations (Groq, OpenAI, Google Gemini)
  - Streaming & Batch processing
  - Structured output extraction using Pydantic
  - Tool creation with `@tool` & function calling
- **`chatbot.ipynb`** — Interactive chat notebook analyzing message types, reasoning tokens, and API error handling.
- **`cloud_env.bat`** — Environment configuration script for setting up cloud SDK and runtime credentials.

---

## 💡 Quick Overview of What Was Done

1. **Reasoning & Metadata Inspection**: Deep-dived into `AIMessage` properties including `additional_kwargs={'reasoning_content': ...}` and `usage_metadata` for detailed token tracking.
2. **Modular Architecture**: Built decoupled, reusable components in `project_1` ready for production integration.
