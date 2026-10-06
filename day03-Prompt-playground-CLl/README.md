# Day 02 — Prompt Playground CLI

## 🎯 What I built
A CLI that runs the *same task* through three prompt strategies so I can
compare how prompting shapes LLM behavior.

## 🧠 Concepts learned

### Old vs. New LangChain
| Old (≤ 0.1) | New (0.2 / 0.3+) |
|---|---|
| `LLMChain` | LCEL: `prompt \| llm \| parser` |
| `PromptTemplate` (strings) | `ChatPromptTemplate` (messages) |
| `FewShotPromptTemplate` | `FewShotChatMessagePromptTemplate` |
| `from langchain.prompts` | `from langchain_core.prompts` |

### New skills
- **Zero-shot** prompting — instruction only.
- **Few-shot** prompting — examples as real message turns, not strings.
- **Role-based** prompting — system persona as a behavioral override.
- **LCEL composition** — same chain, free streaming / async / batching.
- **`.invoke()` universality** — one interface across prompts, models, parsers.

## 🔑 Key takeaway
A prompt is a **program**. Few-shot controls *format*; system role controls *behavior*;
temperature controls *variability*. Master these three and you control the model.

## 🚧 Next
Day 03 — Output Parsers: turning free text into typed, validated data with Pydantic.