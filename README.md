# 📚 Smart Research Assistant

An AI-powered research assistant that helps you:
- Summarize uploaded PDFs or text files
- Ask intelligent questions based on document content
- Challenge yourself with automatically generated MCQs and feedback

Built using:
- **Streamlit** for UI
- **LangChain** with **Groq LLaMA3** for reasoning and summarization
- **PyMuPDF** for PDF reading

---

## 🚀 Features

### 🔍 1. Document Summarization
- Upload a `.pdf` or `.txt` file
- Automatically extracts and summarizes key information using DeepSeek (via Groq API)

### 💬 2. Ask Anything
- Interact in natural language
- Get responses grounded in the uploaded document

### 🧠 3. Challenge Me (MCQ Quiz)
- Auto-generates 3 MCQs based on the document
- User selects answers
- Gives immediate feedback with justification
- Tracks score

---

## 🧰 Folder Structure
```
research/
│
├── app.py                  # Main Streamlit app
├── .env                   # Contains API key for GROQ_API_KEY (not pushed)
├── uploads/               # Stores uploaded files
└── modules/               # Modular LLM logic
    ├── llm.py             # LLM client setup
    ├── summarizer.py      # Text summarization logic
    ├── qna.py             # Q&A logic using LLM
    └── quiz.py            # MCQ generation and evaluation
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/arpit000000/smart-research-assistant.git
cd smart-research-assistant
```

### 2. Setup Conda environment
```bash
conda create -n smart-assistant python=3.12 -y
conda activate smart-assistant
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add `.env` file
Create a file named `.env` and paste:
```env
GROQ_API_KEY=your_actual_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## ✍️ Author
**Arpit Jadon**  
B.Tech CSE (Data Science)
