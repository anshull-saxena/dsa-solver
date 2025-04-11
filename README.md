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
