# Prompt-evaluation-pipeline-for-LLM-outputs.
It takes several business scenarios, runs multiple prompt styles against each scenario, scores the responses with a simple rubric, and saves results to CSV for comparison.

What each part does:

Setup and config
Loads environment variables from .env.
Creates an artifacts folder.
Uses USE_LLM to choose live model calls or offline canned responses.

Provider-aware model setup
Reads LLM_PROVIDER.
If foundry: validates FOUNDRY_ENDPOINT, FOUNDRY_API_KEY, FOUNDRY_MODEL and builds a ChatOpenAI client with normalized base URL.
If azure: validates AZURE_* variables and builds an AzureChatOpenAI client.
If USE_LLM is false: skips model creation.

Test data
Defines 3 sample cases (support metrics, token spike, clinic MVP).
Defines 4 prompt variants (minimal, business-focused, metric-focused, risk-focused).

Execution loop
For each case and each prompt variant, builds a full prompt and invokes the model.
Measures latency per call.
Stores output text plus metadata in a table.
In offline mode, uses predefined responses instead of API calls.

Scoring
Scores each response on:
conciseness
task alignment
metric awareness
actionability
Produces a total score per response.

Summary ranking
Groups by prompt variant.
Computes average score, average word count, and average latency.
Sorts to identify the best variant under this rubric.

Artifact export
Writes detailed results and summary into:
artifacts/prompt_variant_results.csv
artifacts/prompt_variant_summary.csv
