from langchain.chat_models import ChatOpenAI
from agent.state import AgentState
from utils.prompt_utils import SYSTEM_PROMPT
from utils.response_utils import format_response

llm = ChatOpenAI(model="gpt-3.5-turbo")


def generate_response(state: AgentState) -> AgentState:
    user_input = state["user_input"]

    response = llm.invoke([
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_input}
    ])

    formatted = format_response(response.content)

    return {
        "user_input": user_input,
        "result": formatted
    }