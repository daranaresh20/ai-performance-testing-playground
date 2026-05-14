"""
Phase 1 - Python Basics
Calculate performance statistics from response time data.
This mirrors what LoadRunner Summary Reports show — done in Python!
"""
import statistics
from rich.console import Console
from rich.table import Table

console = Console()

# Sample response times in milliseconds (simulate load test results)
response_times = [
    120, 135, 98, 210, 156, 88, 340, 127, 145, 190,
    102, 178, 234, 95, 167, 289, 113, 142, 198, 225,
    88, 156, 302, 118, 134, 167, 245, 92, 178, 211
]

def calculate_percentile(data: list, percentile: float) -> float:
    """Calculate a given percentile from sorted data."""
    sorted_data = sorted(data)
    index = int(len(sorted_data) * (percentile / 100))
    return sorted_data[min(index, len(sorted_data) - 1)]

def generate_stats_report(times: list) -> dict:
    """Generate a full performance statistics report."""
    return {
        "Total Requests": len(times),
        "Min (ms)": min(times),
        "Max (ms)": max(times),
        "Average (ms)": round(statistics.mean(times), 2),
        "Median (ms)": round(statistics.median(times), 2),
        "Std Dev (ms)": round(statistics.stdev(times), 2),
        "P90 (ms)": calculate_percentile(times, 90),
        "P95 (ms)": calculate_percentile(times, 95),
        "P99 (ms)": calculate_percentile(times, 99),
    }

if __name__ == "__main__":
    stats = generate_stats_report(response_times)

    table = Table(title="📊 Performance Test Statistics", show_header=True, header_style="bold cyan")
    table.add_column("Metric", style="bold")
    table.add_column("Value", justify="right")

    for key, value in stats.items():
        table.add_row(key, str(value))

    console.print(table)
    console.print("\n[green]✅ Script complete! This mirrors what LoadRunner summary reports show.[/green]")
