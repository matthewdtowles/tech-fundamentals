class HitCounter:
    WINDOW = 300

    def __init__(self):
        self.times = [0] * self.WINDOW  # ring buffer slot -> second it holds
        self.counts = [0] * self.WINDOW

    def hit(self, timestamp: int) -> None:
        slot = timestamp % self.WINDOW
        if self.times[slot] != timestamp:
            self.times[slot], self.counts[slot] = timestamp, 0
        self.counts[slot] += 1

    def getHits(self, timestamp: int) -> int:
        return sum(c for t, c in zip(self.times, self.counts) if timestamp - t < self.WINDOW)
