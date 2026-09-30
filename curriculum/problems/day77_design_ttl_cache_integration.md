# Architecture + Coding: TTL Cache Inside a Microservice

**Prompt:** Your `catalog` service calls a slow `pricing` service (p99 400 ms).
You add an in-process LRU + TTL cache (like the one you built on day 17 plus a
per-entry expiry). Explain the whole picture as you would in an interview that
mixes architecture and code.

**Timebox:** 45 minutes.

## 1. Where the cache sits
Draw the request path with and without a cache hit:
```
```

## 2. Caching pattern
Cache-aside vs read-through vs write-through vs write-behind. Which one and why?

## 3. Code sketch
The `get_price(sku)` path including TTL check, miss handling and population:
```python
```

## 4. In-process vs distributed (Redis)
| | In-process | Redis |
|---|---|---|
| Latency |  |  |
| Consistency across replicas |  |  |
| Memory |  |  |
| Cold start / deploys |  |  |

## 5. Failure modes
- Cache stampede on a hot key expiring:
- Stale prices after a pricing change (invalidation strategy):
- Pricing service down (serve stale? how stale?):
- Memory pressure:

## 6. What you would measure
Hit rate, p99 with/without hit, eviction rate, staleness…
