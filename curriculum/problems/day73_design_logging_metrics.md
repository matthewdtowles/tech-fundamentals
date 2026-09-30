# Design a Distributed Logging & Metrics Collection System

**Prompt:** Thousands of services on tens of thousands of hosts emit logs and
metrics. Engineers need to search recent logs within seconds, see dashboards and
alerts on metrics, and keep 30 days of logs / 13 months of metrics.

**Timebox:** 45 minutes. Talk it through with Claude, then fill this in.

**Must address:** agent vs sidecar collection, a durable buffer (Kafka) between
producers and storage, at-least-once vs exactly-once and idempotency keys,
hot/warm/cold storage tiers, metric label cardinality, downsampling.

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

