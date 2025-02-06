import subprocess
import hashlib

def git_commit(file_path, task_description):
    task_hash = hashlib.md5(task_description.encode()).hexdigest()[:8]
    subprocess.run(["git", "add", file_path])
    subprocess.run(["git", "commit", "-m", f"Auto-gen: {task_description} (Task-{task_hash})"])
    subprocess.run(["git", "push"])
