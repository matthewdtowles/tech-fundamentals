import time


class TokenBucket:
    def __init__(self, capacity: int, refill_rate: float, clock=time.monotonic):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.clock = clock
        self.tokens = float(capacity)
        self.last = clock()

    def allow(self, tokens: int = 1) -> bool:
        now = self.clock()
        self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.refill_rate)
        self.last = now
        if tokens <= self.tokens:
            self.tokens -= tokens
            return True
        return False
