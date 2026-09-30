# Design a Video Streaming Platform (Netflix-scale)

**Prompt:** Studios upload finished titles. Members on TVs, phones and browsers
worldwide press play and expect video to start in under 2 seconds and never
rebuffer, even on flaky networks.

**Timebox:** 45 minutes.

**Must address:** ingest and transcoding pipeline (chunking, parallel encodes,
bitrate ladder), adaptive bitrate streaming (HLS/DASH manifests), CDN strategy
(Open Connect-style appliances inside ISPs, pre-positioning popular titles
overnight), playback/start-up path, resilience (regional failover, circuit
breakers, bulkheads, chaos engineering).

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

