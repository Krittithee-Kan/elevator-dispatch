"""Builder 2 implements a readable scenario display here."""
from dispatcher import choose_elevator
from scenarios import SCENARIOS
from models import Decision


def run_scenarios(scenarios, output_fn=print) -> list[Decision]:
    """Show each snapshot, call the dispatcher once, display and return decisions."""
    if not scenarios:
        return []

    decisions = []

    for scenario in scenarios:
        output_fn(f"Scenario: {scenario.name}")

        for elevator in scenario.elevators:
            output_fn(
                f"  Elevator {elevator.id}: floor={elevator.floor}, "
                f"direction={elevator.direction}, load_kg={elevator.load_kg}, "
                f"stops={list(elevator.stops)}"
            )

        output_fn(
            f"  Request: floor={scenario.request.floor}, "
            f"direction={scenario.request.direction}"
        )

        decision = choose_elevator(scenario.elevators, scenario.request)

        if decision.elevator_id is None:
            output_fn("  Selected: WAIT")
        else:
            output_fn(f"  Selected: {decision.elevator_id}")

        output_fn(f"  Reason: {decision.reason}")
        output_fn("")

        decisions.append(decision)

    return decisions


if __name__ == "__main__":
    run_scenarios(SCENARIOS)
