# Design a High-Throughput Event Streaming Platform SDK

**Prompt:** Design the client SDK (producer side, plus a consumer sketch) that
thousands of internal services use to publish events to your streaming
platform. Target: 1M events/sec per large service, p99 publish latency < 50 ms,
no silent data loss.

**Timebox:** 45 minutes.

**Must address:** partitioning (key hash vs round robin vs sticky) and per-key
ordering, batching + linger + compression, retries with exponential backoff and
jitter, idempotent producer / dedupe, dead-letter queues, bounded in-memory
buffer and what happens when it is full (block vs drop vs spill), SDK API
ergonomics and versioning.

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

