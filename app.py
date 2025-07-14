import os
import fitz  # PyMuPDF
import streamlit as st
from dotenv import load_dotenv
from modules.summarizer import summarize_text
from modules.qna import ask_deepseek
from modules.quiz import generate_mcqs, evaluate_mcq_answers

# Load environment variables
load_dotenv()

# Extract text from PDF
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join([page.get_text() for page in doc])

# UI
st.set_page_config(page_title="Smart Research Assistant", layout="wide")
st.title("Smart Research Assistant")

uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
# Ensure uploads folder exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

if uploaded_file:
    # Save uploaded file to disk
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File saved to: {file_path}")

    if uploaded_file.name.endswith(".pdf"):
        with st.spinner("Extracting text from PDF..."):
            full_text = extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".txt"):
        full_text = uploaded_file.read().decode("utf-8")
    else:
        st.error("Unsupported file format.")
        st.stop()

    st.success("File uploaded and text extracted!")

    st.subheader("Summary (via LLaMA3 on Groq)")
    with st.spinner("Summarizing using LLM..."):
        summary = summarize_text(full_text)
    st.write(summary)

    mode = st.radio("Choose Interaction Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        st.subheader("Ask Anything (via LLaMA3 on Groq)")
        user_question = st.text_input("Ask a question about this document:")
        if user_question:
            with st.spinner("Thinking with LLM..."):
                answer = ask_deepseek(full_text, user_question)
            st.markdown(f"**Answer:** {answer}")

    elif mode == "Challenge Me":
        st.subheader("🧠 Answer These Questions")

        if st.button("Generate MCQs"):
            questions = generate_mcqs(full_text)

            if questions and isinstance(questions, list) and "question" in questions[0]:
                st.session_state["mcqs"] = questions
                st.session_state["responses"] = {}
            else:
                st.error("⚠️ Failed to generate questions.")

        if "mcqs" in st.session_state:
            for i, q in enumerate(st.session_state["mcqs"]):
                st.markdown(f"**Q{i+1}: {q['question']}**")
                options = q["options"]
                st.session_state["responses"][i] = st.radio(
                    f"Choose an answer for Q{i+1}",
                    options,
                    key=f"q{i}_radio"
                )

            if st.button("Submit Answers"):
                score, feedback = evaluate_mcq_answers(
                    st.session_state["mcqs"],
                    st.session_state["responses"],
                    full_text
                )
                st.success(f"🎯 Your Score: {score}/{len(st.session_state['mcqs'])}")
                for fb in feedback:
                    st.markdown(fb)
