# Day 01: Dynamic Prompt Generator & Structured Output Parser

## Description
A lightweight pipeline demonstrating **LangChain Expression Language (LCEL)** primitives. It formats raw user inputs into structured prompts, streams execution through an LLM, and enforces typed JSON schema output using Pydantic.

## Concepts Learned
- **LCEL (LangChain Expression Language):** Chaining components using standard Unix pipe operator syntax (`|`).
- **`ChatPromptTemplate`:** Building reusable prompt layers separated into System and User roles.
- **`StrOutputParser` & `JsonOutputParser`:** Transforming raw `AIMessage` objects into primitive types and structured JSON.
- **Schema Validation:** Enforcing structured contracts via Pydantic.

## Quickstart
1. Install dependencies:
   ```bash
   pip install langchain langchain-openai python-dotenv pydantic