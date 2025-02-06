import os
from src.orchestrator import orchestrate
from dotenv import load_dotenv
load_dotenv()


if __name__ == "__main__":
    print("🚀 AI-Powered Prototyping Started...")
    orchestrate()
    print("✅ Done! Check GitHub for results.")
