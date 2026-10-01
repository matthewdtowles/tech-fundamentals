from collections import OrderedDict, defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.entries = {}  # key -> [value, freq]
        self.buckets = defaultdict(OrderedDict)  # freq -> keys in LRU order
        self.min_freq = 0

    def _touch(self, key):
        entry = self.entries[key]
        freq = entry[1]
        del self.buckets[freq][key]
        if not self.buckets[freq]:
            del self.buckets[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        entry[1] = freq + 1
        self.buckets[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.entries:
            return -1
        self._touch(key)
        return self.entries[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self.entries:
            self.entries[key][0] = value
            self._touch(key)
            return
        if len(self.entries) == self.capacity:
            evicted, _ = self.buckets[self.min_freq].popitem(last=False)
            if not self.buckets[self.min_freq]:
                del self.buckets[self.min_freq]
            del self.entries[evicted]
        self.entries[key] = [value, 1]
        self.buckets[1][key] = None
        self.min_freq = 1
