import os
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel ,Field

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser , JsonOutputParser
from langchain_openai import ChatOpenAI

#Load environment variables
load_dotenv()

#1. initilaize the llm (Using LCEL)
llm=ChatOpenAI(model_name="gpt-4o-mini",temperature=0.2)

#----PART1 : ext-Based Chain (String Output) ---


string_prompt=ChatPromptTemplate.from_messages([
    ("system","You are an expert technical instructor. Break down concepts concisely."),
    ("user","Explain the concept of {topic} in {num_points} key bullet points.")
])

#build LCEL Chain: prompt -> llm -> Output parser
string_chain= string_prompt | llm | StrOutputParser()

#invoke the chain 
string_result=string_chain.invoke({"topic":"Langchain LCEL", "num_points":3})
print(string_result)

