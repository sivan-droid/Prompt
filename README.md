# LangGraph Agent Example

## Description
This is a simple AI agent built using LangGraph and FastAPI.

## Features
- Prompt-based response generation
- Modular architecture
- Multi-file prompt detection (for validation testing)

## API

### Run Agent
POST /run-agent

Request:
{
  "user_input": "Explain AI"
}

Response:
{
  "result": "AI is..."
}