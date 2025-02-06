import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code(task_description):
    prompt = f"Generate production-ready Python code for this task:\n{task_description}"
    response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user", "content": prompt}], temperature=0.2)
    return response["choices"][0]["message"]["content"].strip()
