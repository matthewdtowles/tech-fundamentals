# Tech Fundamentals

42 days, one problem per day: algorithms, concurrency, system design, behavioral.
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
./tf list        # all 42 days
```

- Progress: `~/.tech-fundamentals/progress.json` (override with `TECH_FUNDAMENTALS_HOME`)
- Your work: `workspace/`
- Content: `curriculum/problems/` (statements + tests), `curriculum/solutions/` (unlocked after you finish a day)

## Modules

| # | Module | Days |
|---|---|---|
| 1 | Hashing & Arrays | 1–2 |
| 2 | Two Pointers & Sliding Window | 3–4 |
| 3 | Binary Search | 5–6 |
| 4 | Linked Lists & Caches | 7–8 |
| 5 | Heaps & Scheduling | 9–10 |
| 6 | Stacks & Parsing | 11–14 |
| 7 | Intervals | 15–16 |
| 8 | Trees | 17–18 |
| 9 | Graphs | 19–22 |
| 10 | Dynamic Programming | 23 |
| 11 | Rate Limiting & Streams | 24–25 |
| 12 | Concurrency | 26–32 |
| 13 | Mock Interviews | 33–34 |
| 14 | System Design | 35–37 |
| 15 | Behavioral & Readiness | 38–42 |

## Development

```
uv run --no-project --python ">=3.10" python -m unittest discover tests
```

`tests/test_curriculum.py` runs every reference solution against its problem's tests,
and checks that every untouched stub fails.
