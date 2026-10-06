# Middleware in LangChain

## What is Middleware?

**Middleware** is a layer of software that sits **between two systems** and intercepts, processes, or transforms data as it flows from one side to the other.

In simple terms:
> Middleware = a "middleman" that runs **before** or **after** the main logic executes.

---

## Middleware in General Programming

```
Request → [Middleware 1] → [Middleware 2] → [Core Logic] → Response
```

Examples:
- Authentication check before an API call
- Logging every request/response
- Rate limiting
- Caching responses

---

## Middleware in LangChain

In LangChain, middleware-like behavior is implemented through **Callbacks**, **Runnables**, and **Hooks** that wrap around model calls, chains, and agents.

### 1. Callbacks (Primary Middleware Mechanism)

Callbacks are the main way LangChain implements middleware. They let you **hook into** events during a chain or model execution.

```python
from langchain_core.callbacks import BaseCallbackHandler

class MyMiddleware(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        print(f"[START] Sending prompt: {prompts}")

    def on_llm_end(self, response, **kwargs):
        print(f"[END] Got response: {response}")

    def on_llm_error(self, error, **kwargs):
        print(f"[ERROR] Something went wrong: {error}")
```

**Usage:**
```python
from langchain_groq import ChatGroq

model = ChatGroq(
    model='llama3-8b-8192',
    callbacks=[MyMiddleware()]
)

response = model.invoke("What is Python?")
```

---

### 2. Key Callback Events (Hooks)

| Event | When it fires |
|-------|---------------|
| `on_llm_start` | Before LLM receives the prompt |
| `on_llm_end` | After LLM returns the response |
| `on_llm_error` | If LLM throws an error |
| `on_chain_start` | Before a chain starts running |
| `on_chain_end` | After a chain finishes |
| `on_chain_error` | If a chain throws an error |
| `on_tool_start` | Before a tool is called |
| `on_tool_end` | After a tool returns a result |
| `on_tool_error` | If a tool throws an error |

---

### 3. LCEL (LangChain Expression Language) as Middleware

LCEL pipes (`|`) let you chain runnables where each step acts as middleware for the next.

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

prompt = ChatPromptTemplate.from_template("Answer this: {question}")
model = ChatGroq(model='llama3-8b-8192')
parser = StrOutputParser()

# Each step is middleware — transforms and passes data to the next
chain = prompt | model | parser

result = chain.invoke({"question": "What is Python?"})
print(result)
```

**Flow:**
```
Input →    [Prompt Template] →  [LLM Model] →  [Output Parser] → Final Output
           (middleware 1)    (middleware 2)   (middleware 3)
```

---

### 4. `with_config()` — Runtime Middleware Configuration

You can pass callbacks at runtime using `with_config()`:

```python
from langchain_core.callbacks import StdOutCallbackHandler

model_with_logging = model.with_config(callbacks=[StdOutCallbackHandler()])
response = model_with_logging.invoke("Explain recursion")
```

---

### 5. Built-in LangChain Middleware Examples

#### a) `StdOutCallbackHandler` — Logs everything to console
```python
from langchain_core.callbacks import StdOutCallbackHandler

handler = StdOutCallbackHandler()
model.invoke("Hello!", config={"callbacks": [handler]})
```

#### b) `FileCallbackHandler` — Logs to a file
```python
from langchain.callbacks import FileCallbackHandler

handler = FileCallbackHandler("output.log")
```

#### c) `LangSmith` — Traces to LangSmith dashboard
```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-api-key"
```
> LangSmith automatically intercepts all calls — it is a cloud-based middleware for observability.

---

## How Middleware Works Internally

```
User calls model.invoke("Hello")
         |
  [on_llm_start] fires  <- Middleware kicks in (logging, auth, etc.)
         |
  Actual API call to Groq/OpenAI
         |
  [on_llm_end] fires    <- Middleware processes the response
         |
  Result returned to user
```

---

## Why Use Middleware?

| Purpose                               | How |
|---------                              |-----|
| **Logging** |  Log every prompt and response |
| **Monitoring** | Track latency, token usage |
| **Caching** | Return cached responses for repeated queries |
| **Rate Limiting** | Throttle API calls |
| **Error Handling** | Catch and handle errors gracefully |
| **Authentication** | Validate API keys before calling LLM |
| **Transformation** | Modify prompts or responses on the fly |

---

## Custom Middleware — Full Example

```python
import time
from langchain_core.callbacks import BaseCallbackHandler
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

class TimingMiddleware(BaseCallbackHandler):
    """Middleware that measures how long the LLM takes to respond."""
    
    def __init__(self):
        self.start_time = None

    def on_llm_start(self, serialized, prompts, **kwargs):
        self.start_time = time.time()
        print("Request started...")

    def on_llm_end(self, response, **kwargs):
        elapsed = time.time() - self.start_time
        print(f"Response received in {elapsed:.2f} seconds")

    def on_llm_error(self, error, **kwargs):
        print(f"Error: {error}")


# Attach middleware to model
model = ChatGroq(
    model='llama3-8b-8192',
    callbacks=[TimingMiddleware()]
)

response = model.invoke([HumanMessage(content="What is machine learning?")])
print(response.content)
```

---

## Summary

| Concept | Description |
|---------|-------------|
| **Middleware** | Code that runs between request and response |
| **Callbacks** | LangChain's primary middleware mechanism |
| **LCEL Pipes** | Chain-style middleware using pipe operator |
| **with_config()** | Attach middleware at runtime |
| **LangSmith** | Cloud-based observability middleware |

> **Key Takeaway:** In LangChain, middleware is not a single class — it is a **pattern** implemented through callbacks, LCEL chains, and configuration hooks that intercept and transform data at various stages of execution.
