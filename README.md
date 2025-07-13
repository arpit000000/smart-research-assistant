# 📚 Smart Research Assistant

An intelligent document assistant that reads PDFs, summarizes them using local NLP models, and answers questions or generates logic-based quizzes using Google Gemini.

---

## 🚀 Features

- 📄 **Upload PDF files**
- 📝 **Summarization** using a local HuggingFace model (no API needed)
- 💬 **Ask Anything** mode powered by Gemini Pro for smart QnA
- 🧠 **Challenge Me** mode:
  - Generates 3 logic/comprehension-based questions from the document
  - Evaluates user answers with detailed feedback & justification (Gemini)

---

## 🧱 Tech Stack

- Streamlit (UI)
- PyMuPDF (PDF text extraction)
- HuggingFace Transformers (local summarization)
- Google Gemini API (QnA & quiz)
- Python Modules + `.env` management

---

## 🗂️ Project Structure

Smart-Research-Assistant/
│
├── app.py                    👉 Streamlit frontend
├── .env.example              👉 Sample API key config
├── requirements.txt
│
└── modules/
    ├── extractor.py          👉 PDF text extraction
    ├── summarizer.py         👉 HuggingFace summarizer
    ├── qna.py                👉 Gemini QnA
    ├── quiz.py               👉 Gemini-based quiz + evaluator
