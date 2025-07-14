from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192"  # ✅ Valid Groq model
)


def ask_deepseek(context, question):
    prompt = f"Context: {context[:3000]}\nQuestion: {question}\nAnswer:"
    response = llm([HumanMessage(content=prompt)])
    return response.content
