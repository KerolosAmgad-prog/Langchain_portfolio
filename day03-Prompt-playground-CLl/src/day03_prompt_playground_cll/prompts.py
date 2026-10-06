"""
Three prompt strategies for the Prompt Playground:
1. zero_shot        - plain instruction
2. final_few_shot   - few-shot with examples as real message turns
3. role_based       - persona-driven system prompt
"""

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import FewShotChatMessagePromptTemplate


# ─────────────────────────────────────────────────────────────
# Strategy A — Zero-Shot
# ─────────────────────────────────────────────────────────────
zero_shot=ChatPromptTemplate([

    ("system","you are a helpful assistant. Answer in exactly one sentence."),
    ("human","{task}")
])

# ─────────────────────────────────────────────────────────────
# Strategy B — Few-Shot (sentiment classification)
# ─────────────────────────────────────────────────────────────
examples =[
    {"input":"I love this product.","output":"POSITIVE"},
    {"input":"Worst purchase ever.","output":"NEGATIVE"},
    {"input":"It's fine, nothing special.","output":"NEUTRAL"},
]

examples_prompt=ChatPromptTemplate([
    ("human","{input}"),
    ("ai","{output}")
])

few_shot=FewShotChatMessagePromptTemplate(
    example_prompt=examples_prompt,
    examples=examples,
)

few_shot_final=ChatPromptTemplate([
    ("system","Classify sentiment. Reply with ONE word: POSITIVE, NEGATIVE, or NEUTRAL."),
    few_shot, #dynamically generate few shot messages
    ("human","{task}")
])
# ─────────────────────────────────────────────────────────────
# Strategy C — Role-Based (persona)
# ─────────────────────────────────────────────────────────────
role_based=ChatPromptTemplate.from_messages([
    ("system","You are Chef Marco — a passionate Italian chef."
    "You answer every question through the lens of cooking and food. "
    "Always mention at least one ingredient. Max 3 sentences."),
    ("human","{task}"),
])


