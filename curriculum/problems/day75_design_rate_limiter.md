# Design a Distributed Rate Limiter

**Prompt:** An API gateway fleet of 200 nodes must enforce limits like
"1,000 requests per minute per API key" and "10,000 per minute per customer
account", globally, with < 5 ms added latency.

**Timebox:** 45 minutes. Reuse what you built on the token bucket and hit counter days.

**Must address:** algorithm choice at scale (token bucket vs sliding window
counter), centralized store (Redis + atomic Lua) vs local counters with periodic
sync, hot keys, fail-open vs fail-closed, response headers (429, Retry-After,
X-RateLimit-Remaining), multi-region.

## 1. Requirements (5 min)
- Functional:
- Non-functional (scale, latency, durability, availability):
- Out of scope:

## 2. Estimates (5 min)
- Traffic (QPS, peak vs average):
- Storage per day / retention:
- Bandwidth:

## 3. API (5 min)
```
```

## 4. Data model (5 min)

## 5. High-level design (10 min)
Components and the path of one request/event through them:

```
```

## 6. Deep dives (10 min)
Pick the two hardest parts and go deep:

## 7. Failure modes & trade-offs (5 min)
| Failure | Detection | Mitigation |
|---|---|---|
|  |  |  |

## 8. What I would do with more time

