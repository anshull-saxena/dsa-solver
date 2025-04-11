#!/usr/bin/env python3
import sys
from gpt4all import GPT4All

# 1️⃣ Change this to match your model filename under ./models/
MODEL_NAME = "models/mistral-7b-instruct.gguf"

def get_solution(question: str, lang: str = "cpp") -> str:
    prompt = (
        f"Problem (DSA):\n{question}\n\n"
        f"Write a complete, working {lang} solution with comments, edge‑case handling, "
        f"and main() driver. Only output code."
    )
    # load once
    global llm
    try:
        llm
    except NameError:
        llm = GPT4All(MODEL_NAME, model_type="gguf")
    resp = llm.generate(prompt, max_tokens=1024, temperature=0.1)
    return resp

def main():
    if len(sys.argv) < 2:
        print("Usage: dsa_solver.py \"Your DSA question here\" [cpp|python]")
        sys.exit(1)

    question = sys.argv[1]
    lang = sys.argv[2] if len(sys.argv) > 2 else "cpp"
    code = get_solution(question, lang)
    print(code)

if __name__ == "__main__":
    main()
