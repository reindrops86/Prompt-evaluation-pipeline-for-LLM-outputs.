# Prompt Variant Comparison Demo

This project compares multiple prompt variants across multiple test cases and scores outputs with a lightweight rubric.

It supports:
- Azure OpenAI deployment mode
- Foundry/OpenAI-compatible endpoint mode
- OpenAI mode
- Offline mode with canned responses for classroom/demo use

## What this does

1. Loads config from .env
2. Creates an LLM client based on LLM_PROVIDER
3. Runs each prompt variant against each sample input
4. Captures responses and latency
5. Scores each response (concise, task alignment, metric awareness, actionable)
6. Saves artifacts as CSV files

## Project structure

- app.py
- artifacts/
- .env
- requirements.txt

## Requirements

- Python 3.10+
- Packages:
  - pandas
  - python-dotenv
  - langchain-openai
  - langchain-core

Example requirements.txt:

pandas
python-dotenv
langchain-openai
langchain-core

## Environment setup

Choose one provider.

Option A: Foundry mode

LLM_PROVIDER=foundry
FOUNDRY_ENDPOINT=https://your-resource.services.ai.azure.com/api/projects/proj-default
FOUNDRY_API_KEY=your_foundry_key
FOUNDRY_MODEL=gpt-5.1
USE_LLM=true

Option B: Azure OpenAI mode

LLM_PROVIDER=azure
AZURE_OPENAI_API_KEY=your_azure_openai_key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_VERSION=2024-12-01-preview
AZURE_OPENAI_CHAT_DEPLOYMENT=your_deployment_name
USE_LLM=true

Option C: OpenAI mode

LLM_PROVIDER=openai
OPENAI_API_KEY=your_openai_key
OPENAI_MODEL=gpt-4.1-mini
USE_LLM=true

Option D: Offline mode

USE_LLM=false

## Run

Install dependencies:

pip install -r requirements.txt

Run:

python app.py

## Output

The script writes:

- artifacts/prompt_variant_results.csv
- artifacts/prompt_variant_summary.csv

The terminal also prints the aggregated summary and the current top variant under this rubric.

## Notes

- Do not commit real API keys.
- Add .env to .gitignore.
- This is a controlled prompt comparison, not a production A/B test.
