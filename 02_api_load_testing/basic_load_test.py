"""
Phase 2 - API Load Testing
Basic HTTP load test using Python requests.
Equivalent to a simple LoadRunner Web HTTP/HTML script.
"""
import time
import requests
import statistics
from rich.console import Console
from rich.progress import Progress

console = Console()

# Config — change this to your target API
TARGET_URL = "https://httpbin.org/get"  # Free test endpoint
NUM_REQUESTS = 20
THINK_TIME_SECONDS = 0.5  # Like LoadRunner think time

def single_request(url: str, session: requests.Session) -> dict:
    """Send one request and return timing data."""
    start = time.time()
    try:
        response = session.get(url, timeout=10)
        end = time.time()
        return {
            "status_code": response.status_code,
            "response_time_ms": round((end - start) * 1000, 2),
            "success": response.status_code == 200
        }
    except requests.RequestException as e:
        return {"status_code": 0, "response_time_ms": 0, "success": False, "error": str(e)}

if __name__ == "__main__":
    console.print(f"[bold cyan]🚀 Starting load test: {NUM_REQUESTS} requests to {TARGET_URL}[/bold cyan]\n")

    results = []
    with requests.Session() as session:
        with Progress() as progress:
            task = progress.add_task("[green]Running requests...", total=NUM_REQUESTS)
            for i in range(NUM_REQUESTS):
                result = single_request(TARGET_URL, session)
                results.append(result)
                progress.advance(task)
                time.sleep(THINK_TIME_SECONDS)

    # Analyze results
    response_times = [r["response_time_ms"] for r in results if r["success"]]
    success_count = sum(1 for r in results if r["success"])

    console.print(f"\n[bold]📊 Load Test Summary[/bold]")
    console.print(f"  Total Requests  : {NUM_REQUESTS}")
    console.print(f"  Passed          : {success_count}")
    console.print(f"  Failed          : {NUM_REQUESTS - success_count}")
    if response_times:
        console.print(f"  Avg Response    : {round(statistics.mean(response_times), 2)} ms")
        console.print(f"  P90 Response    : {sorted(response_times)[int(len(response_times)*0.9)]} ms")
        console.print(f"  Max Response    : {max(response_times)} ms")
