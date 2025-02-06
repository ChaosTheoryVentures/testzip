import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_tasks(prd_text):
    prompt = f"Read the PRD and break it into code-ready tasks:\n{prd_text}"

    response = openai.chat.completions.create(  # ✅ Correct new method
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    tasks_text = response.choices[0].message.content  # ✅ New response format

    with open("tasks.md", "w") as f:
        f.write(tasks_text.strip())

    return tasks_text.strip()
