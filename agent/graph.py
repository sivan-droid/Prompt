from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.nodes import generate_response


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("generate", generate_response)

    graph.set_entry_point("generate")
    graph.add_edge("generate", END)

    return graph.compile()