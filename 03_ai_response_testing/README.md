# Phase 3: Testing AI / LLM API Responses

Validate that AI APIs (ChatGPT, Gemini) return correct, fast, and consistent responses — applying your QA mindset to AI systems.

## Scripts
- `test_llm_response.py` — Call an LLM API and validate: response time, content quality, no hallucinations

## Key Concepts
- LLM APIs are just HTTP REST APIs — you already know how to test these!
- New challenges: response is non-deterministic, need semantic validation
- Measure: latency, token count, response consistency

## Setup
```bash
cp ../.env.example ../.env
# Add your OPENAI_API_KEY to .env
```

## Run
```bash
python test_llm_response.py
```
