from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.history = defaultdict(list)  # key -> [(timestamp, value)] sorted by timestamp

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.history[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        entries = self.history.get(key, [])
        lo, hi, result = 0, len(entries) - 1, ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if entries[mid][0] <= timestamp:
                result = entries[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return result
