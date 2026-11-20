# My dispatch policy

Fill in this template yourself before asking the builders to implement it. Short bullets and a small table are enough. You may discuss ideas or ask AI to challenge them, but make and explain your own choices.

## Priorities

- What I prioritise: I want to reduce unnecessary elevator movement. I prefer to send an elevator that is already moving toward the caller, so it does not need to travel extra distance. I accept that passengers inside that elevator may have one more stop, because this is better than moving a second elevator from far away.
- My exact selection rule: Already has a stop at the caller’s floor If an eligible moving elevator already has the caller’s floor in its stops list, choose it. It does not need any extra stop or extra travel. This is the best choice.
Passing car If no elevator already has that stop, check if an eligible moving elevator is going in the same direction and will pass the caller’s floor. If yes, prefer it over any idle elevator. It needs one extra stop but no extra travel.
Nearest idle elevator If no moving elevator qualifies, choose the idle elevator that is closest to the caller’s floor. Use abs(elevator.floor request.floor) to measure distance. This keeps repositioning travel short.
- My deterministic tie-breaker: If two elevators have the same priority and the same distance, choose the one with the lower letter ID (A before B).
- A tradeoff I accept: People already riding a passing elevator may have to stop one extra time for the new caller. I accept this because sending an idle elevator would use more total movement. I do not claim this saves energy or reduces waiting time exactly it is only a movement-based estimate.

## Predictions before implementation

Use S1, one of S2/S3, and one valid scenario you create in scenarios.py. For your own case, change something meaningful: location, direction, load or scheduled stops. Name it S6.

| Scenario | My expected selection | Why it follows my policy | Benefit and cost / who is affected |
|---|---|---|---|
| S1 | A | A is a passing car (floor 8 moving down, floor 5 is on its path to floor 1). Priority 2 beats priority 3 (idle B). | Benefit: A adds no extra travel. Cost: existing ~2 passengers aboard A gain one more stop. |
| S3 | A | A already has floor 5 in its scheduled stops `(5, 1)`. Priority 1 — zero extra stops. | Benefit: no extra stop or travel whatsoever. Cost: none above what was already planned. |
| S6: Two idle elevators at unequal distances | B | A is idle at floor 2 (3 floors from caller at floor 5); B is idle at floor 6 (1 floor from caller). Both hit priority 3; B wins on distance sub-score. | Benefit: B travels less to reach the caller. Cost: A is left idle; if another call arrives on floors 1–3, response may be slower. |

## Another defensible policy

- An alternative priority: “Nearest elevator first.” Choose the eligible elevator that is currently closest to the caller’s floor, whether it is moving or idle.
- A scenario where it could choose differently, and why: In S1, elevator A is at floor 8 (3 floors above the caller at floor 5), and elevator B is at floor 4 (1 floor below). The nearest-first policy picks B because the distance is smaller (1 < 3). My Route-First policy picks A because A is already moving down toward floor 5 and needs no extra travel. The two policies give different answers here because floor distance alone does not show whether an elevator is already heading toward the caller.

If your predicted choices contradict your general rule, resolve that before implementation. If review later changes your mind, note the revision in EVIDENCE.md and update the policy and code together.
