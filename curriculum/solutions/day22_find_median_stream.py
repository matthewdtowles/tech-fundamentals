import heapq


class MedianFinder:
    def __init__(self):
        self.low = []   # max-heap (negated): lower half
        self.high = []  # min-heap: upper half; len(low) == len(high) or len(high) + 1

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2
