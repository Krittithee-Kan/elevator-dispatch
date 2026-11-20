"""Builder 1 implements the student's policy here."""
from models import Elevator, Request, Decision
from rules import eligible_ids

def choose_elevator(elevators: tuple[Elevator, Elevator], request: Request) -> Decision:
    """Choose one eligible elevator according to POLICY.md; never mutate inputs."""
    ids = set(eligible_ids(elevators, request))

    if not ids:
        return Decision(None, "No eligible elevator available for this request")

    eligible = [e for e in elevators if e.id in ids]

    # Priority 1: moving elevator that already has the caller's floor in its stops
    already_stopping = [e for e in eligible if e.direction != "idle" and request.floor in e.stops]
    if already_stopping:
        chosen = min(already_stopping, key=lambda e: e.id)
        return Decision(chosen.id, f"Elevator {chosen.id} is already stopping at floor {request.floor}")

    # Priority 2: moving elevator passing through the caller's floor (direction matches, floor on route)
    passing = [e for e in eligible if e.direction != "idle"]
    if passing:
        chosen = min(passing, key=lambda e: e.id)
        return Decision(chosen.id, f"Elevator {chosen.id} is passing floor {request.floor} going {chosen.direction}")

    # Priority 3: idle elevator closest to the caller's floor
    idle = [e for e in eligible if e.direction == "idle"]
    if idle:
        chosen = min(idle, key=lambda e: (abs(e.floor - request.floor), e.id))
        return Decision(chosen.id, f"Idle elevator {chosen.id} is closest to floor {request.floor} (distance {abs(chosen.floor - request.floor)})")

    return Decision(None, "No eligible elevator available for this request")
