from modules.llm import llm
from langchain_core.messages import HumanMessage
import json
import re

def generate_mcqs(context):
    prompt = f"""
You are a quiz generator.

Given the document below, generate 3 multiple-choice questions. For each question, include:
1. A question
2. Four options labeled A, B, C, D
3. The correct answer letter
4. A brief explanation

Return the result as a JSON list like:
[
  {{
    "question": "...",
    "options": ["A) ...", "B) ...", "C) ...", "D) ..."],
    "answer": "B",
    "explanation": "..."
  }},
  ...
]

Document:
{context[:3000]}
"""
    response = llm([HumanMessage(content=prompt)])
    raw_output = response.content
    print("📤 Raw MCQ output:\n", raw_output)

    # Try to extract the JSON array between square brackets
    try:
        json_block = re.search(r'\[(.|\n)*\]', raw_output)
        if json_block:
            questions = json.loads(json_block.group(0))
            return questions
        else:
            raise ValueError("No JSON array found.")
    except Exception as e:
        print("❌ JSON parsing error:", e)
        return [{
            "question": "Failed to generate MCQs.",
            "options": ["A) Option 1", "B) Option 2", "C) Option 3", "D) Option 4"],
            "answer": "A",
            "explanation": f"Raw output: {raw_output[:500]}"  # limit output for debugging
        }]
def evaluate_mcq_answers(questions, user_answers, context):
    score = 0
    feedback = []

    for i, q in enumerate(questions):
        correct = q["answer"]
        selected = user_answers.get(i, "")[0]  # Extract 'A', 'B', etc.

        if selected == correct:
            score += 1
            feedback.append(f"✅ Correct! {q['explanation']}")
        else:
            feedback.append(f"❌ Incorrect. Correct answer: {correct}. {q['explanation']}")

    return score, feedback
