import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_tasks(prd_text):
    prompt = f"Read the PRD and break it into code-ready tasks:\n{prd_text}"
    response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}], temperature=0.3)
    return response["choices"][0]["message"]["content"].strip()
