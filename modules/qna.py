import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-2.0-flash")

def ask_gemini(context, question):
    try:
        response = gemini_model.generate_content([context[:3000], question])
        return response.text if hasattr(response, "text") else str(response)
    except Exception as e:
        return f"⚠️ Gemini error: {e}"
