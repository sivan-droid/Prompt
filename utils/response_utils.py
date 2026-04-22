FORMAT_PROMPT = """
You are a response formatter.

Instructions:
- Clean the response
- Remove unnecessary words
- Make output readable
"""


def format_response(text: str) -> str:
    return text.strip()