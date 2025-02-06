import os
from src.llm.task_decomposer import generate_tasks
from src.llm.code_generator import generate_code
from src.git_handler import git_commit
from src.executor import execute_code

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

def orchestrate():
    prd_text = read_file("README.md")
    tasks_text = generate_tasks(prd_text)
    write_file("tasks.md", tasks_text)

    with open("tasks.md", "r", encoding="utf-8") as f:
        tasks = [line.strip()[5:] for line in f.readlines() if line.startswith("- [ ]")]

    for task in tasks:
        code = generate_code(task)
        filename = task.lower().replace(" ", "_").replace("/", "_")[:50] + ".py"
        file_path = os.path.join("generated_code", filename)

        os.makedirs("generated_code", exist_ok=True)
        write_file(file_path, code)

        output, error = execute_code(file_path)
        if not error:
            git_commit(file_path, task)
