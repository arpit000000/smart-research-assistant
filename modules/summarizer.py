from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    try:
        chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
        summaries = [summarizer(chunk)[0]['summary_text'] for chunk in chunks[:3]]
        return "\n".join(summaries)
    except Exception as e:
        return f"⚠️ Local summarization failed: {e}"
