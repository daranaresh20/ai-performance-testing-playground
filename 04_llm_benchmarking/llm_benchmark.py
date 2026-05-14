"""
Phase 4 - LLM Benchmarking
Measure LLM API performance: latency, throughput, percentiles.
Directly maps your LoadRunner metrics knowledge to AI APIs.
"""
import time
import statistics
import csv
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.table import Table

console = Console()

# Benchmark config
NUM_RUNS = 10
TEST_PROMPT = "In one sentence, what is performance testing?"
OUTPUT_DIR = Path("benchmark_results")
OUTPUT_DIR.mkdir(exist_ok=True)

def simulate_llm_call(prompt: str) -> dict:
    """
    Simulates an LLM API call with realistic latency.
    Replace with actual OpenAI/Gemini API call.
    """
    import random
    time.sleep(random.uniform(0.2, 1.5))  # Simulated variable latency
    tokens = random.randint(20, 80)
    return {
        "latency_ms": round(random.uniform(200, 1500), 2),
        "tokens": tokens,
        "tps": round(tokens / random.uniform(0.2, 1.5), 2),
        "success": random.random() > 0.05  # 5% error rate simulation
    }

def run_benchmark():
    console.print(f"[bold cyan]⚡ LLM Benchmark: {NUM_RUNS} runs[/bold cyan]\n")
    results = []

    for i in range(1, NUM_RUNS + 1):
        console.print(f"  Run {i}/{NUM_RUNS}...", end=" ")
        result = simulate_llm_call(TEST_PROMPT)
        results.append(result)
        status = "[green]✓[/green]" if result["success"] else "[red]✗[/red]"
        console.print(f"{status} {result['latency_ms']}ms | {result['tokens']} tokens")

    # Calculate stats
    latencies = [r["latency_ms"] for r in results if r["success"]]
    success_count = sum(1 for r in results if r["success"])

    stats = {
        "Total Runs": NUM_RUNS,
        "Successful": success_count,
        "Error Rate": f"{round((1 - success_count/NUM_RUNS)*100, 1)}%",
        "Avg Latency (ms)": round(statistics.mean(latencies), 2),
        "P50 Latency (ms)": round(statistics.median(latencies), 2),
        "P95 Latency (ms)": sorted(latencies)[int(len(latencies)*0.95)-1] if latencies else 0,
        "P99 Latency (ms)": sorted(latencies)[int(len(latencies)*0.99)-1] if latencies else 0,
        "Min Latency (ms)": min(latencies),
        "Max Latency (ms)": max(latencies),
    }

    # Display table
    table = Table(title="\n📊 LLM Benchmark Results", header_style="bold magenta")
    table.add_column("Metric")
    table.add_column("Value", justify="right")
    for k, v in stats.items():
        table.add_row(k, str(v))
    console.print(table)

    # Save CSV report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = OUTPUT_DIR / f"benchmark_{timestamp}.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    console.print(f"\n[green]📁 Report saved: {csv_path}[/green]")

if __name__ == "__main__":
    run_benchmark()
