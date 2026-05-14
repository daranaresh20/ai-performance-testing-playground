# Phase 2: API Load Testing with Python

Replace your LoadRunner scripts with Python-based HTTP load tests.

## Scripts
- `basic_load_test.py` — Sequential HTTP load test using `requests`
- `async_load_test.py` — Concurrent load test using `aiohttp` (much faster!)

## Key Concepts
- `requests` library = your Python alternative to Web/HTTP protocol in LoadRunner
- `aiohttp` = async/concurrent requests (like VUser concurrency in LoadRunner)
- Collecting and reporting response times

## Run
```bash
python basic_load_test.py
python async_load_test.py
```
