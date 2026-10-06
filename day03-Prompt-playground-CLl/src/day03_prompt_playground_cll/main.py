"""
Prompt Playground CLI
Run the same task through 3 prompt strategies and compare outputs.
"""
import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from prompts import zero_shot,few_shot_final,role_based 



# ─────────────────────────────────────────────────────────────
# 1. Load environment
# ─────────────────────────────────────────────────────────────
load_dotenv()
USE_OLLAMA= os.getenv("USE_OLLAMA","false").lower()=="true"


# ─────────────────────────────────────────────────────────────
# 2. Initialize the chat model
# ─────────────────────────────────────────────────────────────
if USE_OLLAMA :
    from langchain_ollama import ChatOllama
    llm=ChatOllama(model="gemma3:270m",temperature=0.3)
    print("LLM is OLLAMA model")
else :
    llm=ChatOpenAI(model="gpt-4o-mini",temperature=0.3) # LLM model 
    print("LLM is OpenAI model")


# ─────────────────────────────────────────────────────────────
# 3. Wire LCEL chains
# ─────────────────────────────────────────────────────────────
parser= StrOutputParser()
chains={
    "zero-shot":  zero_shot      | llm | parser,
    "few-shot":   few_shot_final | llm | parser,
    "role-based": role_based     | llm | parser,
}

# ─────────────────────────────────────────────────────────────
# 4. CLI
# ─────────────────────────────────────────────────────────────
def run():
    print("type a task, pick a mode.\n")
    print("Modes: [1] zero-shot  [2] few-shot  [3] role-based  [4] compare all\n")
    while True :
        task = input("Task : ").strip()
        if task.lower() in {"exit" ,"quit"} :
            break 

        mode = input("Mode (1/2/3/4): ").strip()

        if mode == "4" :
            for name , chain in chains.items():
                print(f"\n{name.upper()}")
                print(chain.invoke({"task":task}))
        else :

            key ={"1": "zero-shot", "2": "few-shot", "3": "role-based"}.get(mode)
            if not key :
                print("Invalid mode .please try again")
                continue
            print(f"\n {key.upper()}")
            print(chains[key].invoke({"task":task}))
            print()
if __name__ =="__main__" :
    run()