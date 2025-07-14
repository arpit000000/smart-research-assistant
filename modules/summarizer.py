from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
from langchain.schema import HumanMessage
import os

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192"  
)


def summarize_text(text):
    prompt = f"Summarize the following document in one paragraph:\n{text[:3000]}"
    response = llm([HumanMessage(content=prompt)])
    return response.content
