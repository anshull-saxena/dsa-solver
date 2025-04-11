# Offline DSA Solver

An offline CLI tool that uses GPT4All to generate Data Structures & Algorithms solutions in C++ or Python.

## Prerequisites

- Python 3.8+
- `pip install gpt4all`

## Setup

1. **Download a quantized model**  
   Go to https://gpt4all.io/models/ and grab e.g. `mistral-7b-instruct.gguf`.  
   Place it in `models/` so you have `models/mistral-7b-instruct.gguf`.

2. **Install dependencies**  
   ```bash
   pip install gpt4all


SETUP

---

## 4. Installation Steps

```bash
git clone <this‑repo‑url> dsa_solver
cd dsa_solver

# 1. Put your GGUF model under ./models/
#    e.g. models/mistral-7b-instruct.gguf

pip install gpt4all

chmod +x dsa_solver.py

# 2. Run it:
./dsa_solver.py "Write a recursive C++ function for merge sort" cpp
