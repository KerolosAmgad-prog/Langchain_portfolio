# Day 02 — Hello LangChain CLI Chat

## 🎯 What I built
A CLI chatbot using LangChain's LCEL, with a system persona and in-session memory.

## 🧠 Concepts learned
- `ChatOpenAI` / `ChatOllama` — model-agnostic chat models
- `ChatPromptTemplate` + `MessagesPlaceholder` — parameterized prompts
- LCEL (`prompt | llm | StrOutputParser`) — composable chains
- Message roles: system / human / ai

## 🔑 Key takeaway
Every LangChain app = **Prompt → Model → Output**, wired with `|`.

## 🚧 Next
Day 02: prompt engineering patterns (few-shot, role prompting).