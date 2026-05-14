"""
Phase 6 - SRE Observability
Calculate SLO compliance and error budget.
This is the SRE version of your LoadRunner pass/fail criteria!
"""
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# --- Define your SLOs (like your performance acceptance criteria in LoadRunner) ---
SLOS = {
    "Availability": {"target_pct": 99.9, "description": "System uptime"},
    "P95 Latency < 500ms": {"target_pct": 95.0, "description": "95% of requests under 500ms"},
    "Error Rate < 1%": {"target_pct": 99.0, "description": "Less than 1% errors"},
}

# --- Simulated measurement data (replace with real metrics from your load tests) ---
MEASUREMENTS = {
    "Availability": 99.85,       # Actual uptime %
    "P95 Latency < 500ms": 96.2, # % of requests meeting the latency SLO
    "Error Rate < 1%": 98.7,     # % of requests that were successful
}

MONTHLY_MINUTES = 43800  # Minutes in a 30-day month

def calculate_error_budget(target_pct: float, actual_pct: float) -> dict:
    """Calculate error budget consumption."""
    allowed_failure_pct = 100 - target_pct
    actual_failure_pct = 100 - actual_pct
    if allowed_failure_pct == 0:
        budget_remaining_pct = 0 if actual_failure_pct > 0 else 100
    else:
        budget_consumed_pct = (actual_failure_pct / allowed_failure_pct) * 100
        budget_remaining_pct = max(0, 100 - budget_consumed_pct)
    budget_remaining_minutes = (budget_remaining_pct / 100) * (allowed_failure_pct / 100) * MONTHLY_MINUTES
    return {
        "budget_remaining_pct": round(budget_remaining_pct, 1),
        "budget_remaining_minutes": round(budget_remaining_minutes, 1)
    }

if __name__ == "__main__":
    console.print(Panel("[bold cyan]SRE SLO Compliance Dashboard[/bold cyan]", expand=False))

    table = Table(show_header=True, header_style="bold")
    table.add_column("SLO")
    table.add_column("Target", justify="right")
    table.add_column("Actual", justify="right")
    table.add_column("Status")
    table.add_column("Error Budget Left")

    for slo_name, slo_config in SLOS.items():
        target = slo_config["target_pct"]
        actual = MEASUREMENTS[slo_name]
        met = actual >= target
        budget = calculate_error_budget(target, actual)
        status = "[green]✅ MET[/green]" if met else "[red]❌ BREACHED[/red]"
        budget_color = "green" if budget["budget_remaining_pct"] > 20 else "yellow" if budget["budget_remaining_pct"] > 0 else "red"
        table.add_row(
            slo_name,
            f"{target}%",
            f"{actual}%",
            status,
            f"[{budget_color}]{budget['budget_remaining_pct']}% ({budget['budget_remaining_minutes']} min)[/{budget_color}]"
        )

    console.print(table)
    console.print("\n[dim]Tip: This is the SRE version of your LoadRunner Pass/Fail summary report![/dim]")
