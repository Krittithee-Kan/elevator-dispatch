# My dispatch policy

Fill in this template yourself before asking the builders to implement it. Short bullets and a small table are enough. You may discuss ideas or ask AI to challenge them, but make and explain your own choices.

## Priorities

- What I prioritise: [whose experience or which resource matters most]
- My exact selection rule: [ordered rules or a defined cost formula, applied after eligibility]
- My deterministic tie-breaker: [what happens if candidates remain equal]
- A tradeoff I accept: [who may receive worse service, or what may cost more]

## Predictions before implementation

Use S1, one of S2/S3, and one valid scenario you create in scenarios.py. For your own case, change something meaningful: location, direction, load or scheduled stops. Name it S6.

| Scenario | My expected selection | Why it follows my policy | Benefit and cost / who is affected |
|---|---|---|---|
| S1 | A | A is a passing car (floor 8 moving down, floor 5 is on its path to floor 1). Priority 2 beats priority 3 (idle B). | Benefit: A adds no extra travel. Cost: existing ~2 passengers aboard A gain one more stop. |
| S3 | A | A already has floor 5 in its scheduled stops `(5, 1)`. Priority 1 — zero extra stops. | Benefit: no extra stop or travel whatsoever. Cost: none above what was already planned. |
| S6: Two idle elevators at unequal distances | B | A is idle at floor 2 (3 floors from caller at floor 5); B is idle at floor 6 (1 floor from caller). Both hit priority 3; B wins on distance sub-score. | Benefit: B travels less to reach the caller. Cost: A is left idle; if another call arrives on floors 1–3, response may be slower. |

## Another defensible policy

- An alternative priority: [briefly describe it]
- A scenario where it could choose differently, and why: [use or adapt a case]

If your predicted choices contradict your general rule, resolve that before implementation. If review later changes your mind, note the revision in EVIDENCE.md and update the policy and code together.
