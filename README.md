# Log Report Terminal-Bench Task

This repository contains a corrected Terminal-Bench 2 task for parsing an Apache-style access log into a JSON summary report.

## Task

The agent reads:

```text
/app/access.log
```

and produces:

```text
/app/report.json
```

The report contains:

- `total_requests`: number of non-empty log entries
- `unique_ips`: number of distinct client IP addresses
- `top_path`: most frequently requested path

## Repository structure

```text
log-report/
├── environment/
│   ├── Dockerfile
│   └── access.log
├── solution/
│   ├── solve.py
│   └── solve.sh
├── tests/
│   ├── test_outputs.py
│   └── test.sh
├── instruction.md
├── task.toml
└── README.md
```

## Corrections made

- Changed `artifacts` to a TOML array pointing to `/app/report.json`.
- Replaced the unpinned Python base image with an approved image pinned by SHA-256 digest.
- Removed `environment/solution_hint.py` to prevent leaking the reference solution.
- Replaced the existence-only verifier with tests that validate the report schema and values.
- Updated the verifier to write `reward.txt` and `ctrf.json` under `/logs/verifier/`.
- Rewrote `instruction.md` with three numbered success criteria aligned one-to-one with the tests.

## Running the task

From inside the `log-report` directory, run the Oracle agent:

```bash
harbor run -p . -a oracle
```

Expected reward:

```text
1.0
```

Run the no-op agent:

```bash
harbor run -p . --agent nop
```

Expected reward:

```text
0.0
```

## Verification results

### Oracle

```text
reward.txt: 1
tests: 3
passed: 3
failed: 0
```

### Nop

```text
reward.txt: 0
tests: 3
passed: 0
failed: 3
```

These results confirm that the reference solution passes while an agent that produces no output fails.
