# Tech Fundamentals

83 days, one problem per day: algorithms, concurrency, system design, behavioral.
Each day goes **learn → quiz → discuss → solve**, and you cannot skip ahead.

## Start

In Claude Code, from this directory:

```
/fundamentals
```

Claude briefly introduces the topic, quizzes you (you need 2/2 to move on), and discusses
your approach. Then you solve a Python file whose tests and goal runtime are at the top.

## CLI

Requires [uv](https://docs.astral.sh/uv/). It runs on Python 3.10+ automatically.

```
./tf status      # where am I
./tf show        # today's brief
./tf check       # run my tests; passing completes the day
./tf list        # all 83 days
```

- Progress: `~/.tech-fundamentals/progress.json` (override with `TECH_FUNDAMENTALS_HOME`)
- Your work: `workspace/`
- Content: `curriculum/problems/` (statements + tests), `curriculum/solutions/` (unlocked after you finish a day)

## Modules

| # | Module | Days |
|---|---|---|
| 1 | Hashing & Arrays | 1–5 |
| 2 | Two Pointers & Sliding Window | 6–10 |
| 3 | Binary Search | 11–14 |
| 4 | Linked Lists & Caches | 15–18 |
| 5 | Heaps & Scheduling | 19–23 |
| 6 | Stacks & Parsing | 24–29 |
| 7 | Intervals | 30–32 |
| 8 | Trees | 33–37 |
| 9 | Backtracking | 38–40 |
| 10 | Tries | 41–42 |
| 11 | Graphs | 43–50 |
| 12 | Dynamic Programming & Greedy | 51–58 |
| 13 | Rate Limiting & Streams | 59–61 |
| 14 | Concurrency | 62–69 |
| 15 | Mock Interviews | 70–72 |
| 16 | System Design | 73–77 |
| 17 | Behavioral & Readiness | 78–83 |

## Development

```
uv run --no-project --python ">=3.10" python -m unittest discover tests
```

`tests/test_curriculum.py` runs every reference solution against its problem's tests,
and checks that every untouched stub fails.
