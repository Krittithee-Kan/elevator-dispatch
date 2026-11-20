# My experiment results

Fill in this template with actual observations. Short bullets are sufficient.

Name / student ID: Krittithee Kanjanapinchote 6580988

Tool, visible software version and model(s): Claude sonnet 4.6

Route: Separate sessions with manual coordination (two builder agents run one at a time, one reviewer agent)

## Agent outputs

| Role | What it delivered | Brief excerpt or screenshot link |
|---|---|---|
| Dispatcher builder | Wrote the choose_elevator function using three priority steps from POLICY.md | "Priority 1: already stopping, Priority 2: passing car, Priority 3: nearest idle" |
| Display builder | Wrote the run_scenarios function to show each elevator, the request, and the decision | "Selected: A / Reason: Elevator A is passing floor 5 going down" |
| Reviewer | Checked the code and found one small code issue, one accepted tradeoff, and one gap in the policy | "Priority 2 always picks a passing elevator even if it is far away" |

## Compare with my predictions

| Scenario | Expected selection | Actual selection and reason | Matches my policy? |
|---|---|---|---|
| S1 | A | A  — Elevator A is passing floor 5 going down | Yes |
| S3 | A | A  — Elevator A already has floor 5 in its stops | Yes |
| S6 | B | B  — Idle elevator B is closest to floor 5 (distance 1) | Yes |

- Supplied suite command and actual result: py -m unittest -v → 6 out of 6 tests passed
- One review finding or concern I checked: The reviewer said that Priority 2 can send a far elevator instead of a close idle one. I checked my POLICY.md and it says to always prefer a passing elevator over an idle one, with no distance limit. This is not a code mistake. It is a gap in my written policy. I accept it because my main goal is to avoid extra elevator travel, not to reduce the caller's waiting time.
- Change made, if needed: No code change was needed. The code follows the policy correctly. I recorded the limitation here instead.
- Does my policy serve my stated priority? Yes. In S1, elevator A is already moving down past floor 5, so it needs no extra travel. This matches my goal of reducing unnecessary movement. The cost is that passengers already inside A have one more stop.
- What did I have to coordinate between the agents? The dispatcher builder had to finish first. I then gave the finished dispatcher.py to the display builder so it could call choose_elevator correctly.
