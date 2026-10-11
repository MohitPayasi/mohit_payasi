"""
main.py - LangGraph Project Entry Point

This is the main entry point for the LangGraph agent project.
It builds a StateGraph, compiles it, and runs an example workflow.
"""

import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated, List
import operator

from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END, START

# ─── Load environment variables ───────────────────────────────────────────────
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

# Optional: Enable LangSmith tracing
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "langgraph-project"


# ─── State Schema ─────────────────────────────────────────────────────────────

class AgentState(TypedDict):
    """
    State shared across all nodes in the graph.

    Fields:
        messages (List[BaseMessage]): Conversation message history.
        next_step (str): Routing signal used by conditional edges.
    """
    messages: Annotated[List[BaseMessage], operator.add]
    next_step: str


# ─── LLM Setup ────────────────────────────────────────────────────────────────

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=GOOGLE_API_KEY,
    temperature=0.7,
)


# ─── Node Functions ───────────────────────────────────────────────────────────

def call_llm(state: AgentState) -> AgentState:
    """
    Node: Calls the LLM with the current messages in state.

    Args:
        state (AgentState): Current graph state.

    Returns:
        AgentState: Updated state with the LLM response appended.
    """
    messages = state["messages"]
    response: AIMessage = llm.invoke(messages)
    return {"messages": [response], "next_step": "end"}


def router(state: AgentState) -> str:
    """
    Conditional edge function: Decides the next node based on state.

    Args:
        state (AgentState): Current graph state.

    Returns:
        str: Name of the next node to route to.
    """
    return state.get("next_step", "end")


# ─── Build the Graph ──────────────────────────────────────────────────────────

def build_graph() -> StateGraph:
    """
    Builds and compiles the LangGraph StateGraph.

    Returns:
        CompiledGraph: The compiled, runnable LangGraph.
    """
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("llm_node", call_llm)

    # Add edges
    workflow.add_edge(START, "llm_node")
    workflow.add_conditional_edges(
        "llm_node",
        router,
        {"end": END},
    )

    return workflow.compile()


# ─── Main Entry ───────────────────────────────────────────────────────────────

def main():
    """
    Main function: Runs the compiled LangGraph agent with a sample question.
    """
    print("=" * 50)
    print("  LangGraph Agent - Starting...")
    print("=" * 50)

    graph = build_graph()

    # Initial user message
    initial_state: AgentState = {
        "messages": [HumanMessage(content="What is LangGraph and why is it useful?")],
        "next_step": "",
    }

    print("\n[USER]: What is LangGraph and why is it useful?\n")

    # Run the graph
    result = graph.invoke(initial_state)

    # Print the final AI response
    final_message = result["messages"][-1]
    print(f"[AI]: {final_message.content}")
    print("\n" + "=" * 50)
    print("  Done.")
    print("=" * 50)


if __name__ == "__main__":
    main()
