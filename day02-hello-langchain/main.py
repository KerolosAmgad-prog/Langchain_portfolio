# main .py

#step1 : load Environment
import os 
from dotenv import load_dotenv
load_dotenv()
USE_OLLAMA = os.getenv('USE_OLLAMA','False').lower() == 'true' # the value is True so it will pass to ollama 


#step2 : Initialize the Chat Model
if USE_OLLAMA :
    from langchain_ollama import ChatOllama
    llm=ChatOllama(model='gemma3:270m',temperature=0.7)
    print("Using ollama models ")
else :
    from langchain_openai import ChatOpenAI
    llm =ChatOpenAI(model='gpt-4o-mini',temperature=0.7)
    print("Using openai models ")

#Step3 : Build the Prompt Template
from langchain_core.prompts import ChatPromptTemplate ,MessagesPlaceholder
prompt= ChatPromptTemplate.from_messages([
    ("system","You are 'Aria', a friendly and concise AI tutor. "
     "Explain things simply, use short examples, and never exceed 4 sentences "
     "unless the user asks for depth."),
    MessagesPlaceholder(variable_name="history"),
    ("human","{input}"),
])



#step4 : Compose the chain with LCEL 
from langchain_core.output_parsers import StrOutputParser
chain =prompt | llm | StrOutputParser()

#step5 : Add Simple in session Memory
from langchain_core.messages import HumanMessage ,AIMessage
history=[]
def chat (user_input:str) -> str :
    response= chain.invoke({"input":user_input,"history":history})
    history.append(HumanMessage(content=user_input))
    history.append (AIMessage(content=response))
    return response

#step 6 : The CLI Loop
def main():
    print("Aria is ready , type 'exit' to quit.\n")
    while True :
        try :
            user_input = input("you: ").strip()
        except(KeyboardInterrupt,EOFError):
            print("\n Bye")
            break
        if user_input.lower () in {"exit","quit"} :
            print("Bye!")
            break
        if not user_input:
            continue
        reply=chat(user_input)
        print(f"Aria : {reply}\n")

if __name__=="__main__":
    main()   
   
