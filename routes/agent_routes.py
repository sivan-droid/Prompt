from fastapi import APIRouter
from agent.graph import build_graph

router = APIRouter()

graph = build_graph()


@router.post("/run-agent")
def run_agent(payload: dict):
    user_input = payload.get("user_input", "")

    result = graph.invoke({
        "user_input": user_input
    })

    return result