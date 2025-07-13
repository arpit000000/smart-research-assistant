import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

def generate_questions_from_doc(text):
    prompt = f"Generate 3 logic-based or comprehension-focused questions from the document:\n{text[:3000]}"
    response = gemini_model.generate_content(prompt)
    return response.text.strip().split("\n")

def evaluate_answer_with_gemini(question, user_answer, context):
    prompt = (
        f"Document: {context[:3000]}\n"
        f"Question: {question}\n"
        f"User Answer: {user_answer}\n"
        f"Evaluate the answer and give feedback with justification."
    )
    response = gemini_model.generate_content(prompt)
    return response.text.strip()
