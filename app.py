# app.py — Modular Streamlit Frontend

import os
import streamlit as st
from dotenv import load_dotenv
from modules.extractor import extract_text_from_pdf
from modules.summarizer import summarize_text
from modules.qna import ask_gemini
from modules.quiz import generate_questions_from_doc, evaluate_answer_with_gemini
import google.generativeai as genai

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# UI
st.set_page_config(page_title="Smart Research Assistant", layout="wide")
st.title("📚 Smart Research Assistant")

uploaded_file = st.file_uploader("📤 Upload a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("🔍 Extracting text..."):
        full_text = extract_text_from_pdf(uploaded_file)

    st.success("✅ File uploaded and text extracted!")

    st.subheader("📝 Local Model Summary")
    with st.spinner("Summarizing using local model..."):
        summary = summarize_text(full_text)
    st.write(summary)

    mode = st.radio("Choose Interaction Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        st.subheader("💬 Ask Anything (Gemini)")
        user_question = st.text_input("Ask a question about this document:")
        if user_question:
            with st.spinner("Thinking with Gemini..."):
                answer = ask_gemini(full_text, user_question)
            st.markdown(f"**🧠 Gemini Answer:** {answer}")

    elif mode == "Challenge Me":
        st.subheader("🧠 Answer These Questions")
        questions = generate_questions_from_doc(full_text)
        for i, q in enumerate(questions):
            if q.strip():
                user_answer = st.text_input(f"Q{i+1}: {q}", key=f"q_{i}")
                if user_answer:
                    feedback = evaluate_answer_with_gemini(q, user_answer, full_text)
                    st.markdown(f"**Feedback:** {feedback}")
