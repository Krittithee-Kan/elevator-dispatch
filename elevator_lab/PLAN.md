# My agent plan

Fill in the brackets before delegation. This is a template, not a completed plan.

- **Dispatcher builder owns dispatcher.py**: Write the `choose_elevator` function. Use `rules.eligible_ids` to find which elevators can be used. Then follow the Route-First policy from POLICY.md. First, pick the elevator that already has a stop at the caller's floor. Second, pick a moving elevator that is going past the caller. Third, pick the nearest idle elevator. If no elevator can be used, return `Decision(None, reason)`.

- **Display builder owns app.py**: Write the `run_scenarios` function. For each scenario, show the name, both elevators' information, and the request. Call `choose_elevator` one time only. Then show `Selected: A`, `Selected: B`, or `Selected: WAIT`. Also show the reason. Return all decisions as a list.

- **Reviewer is read-only after both files are done**: Check three things. First, does the code use `eligible_ids` correctly? Second, does it follow the three priorities in POLICY.md? Third, does the display show everything that SPEC.md R4 requires? Also find one tradeoff in the policy using a real scenario. Write at most three problems. Say if each problem is a code mistake, a policy mistake, or a tradeoff. Do not change any files.

- **Handoff steps**: I give both builders the files they need: SPEC.md, POLICY.md, PLAN.md, models.py, rules.py, scenarios.py, and their own file. Each builder only changes their own file. After both finish, I run `python -m unittest -v` and `python app.py` and check the results before giving the code to the reviewer.

- **Final check**: I compare the output of `python app.py` for S1, S3, and S6 with my predictions in POLICY.md. If any result is different from what I expected, I will check why before I fill in EVIDENCE.md.
