import threading
from collections import OrderedDict


class ThreadSafeLRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = OrderedDict()
        self.lock = threading.Lock()  # get() mutates recency, so one exclusive lock

    def _store(self, key, value):
        self.data[key] = value
        self.data.move_to_end(key)
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)

    def get(self, key):
        with self.lock:
            if key not in self.data:
                return None
            self.data.move_to_end(key)
            return self.data[key]

    def put(self, key, value) -> None:
        with self.lock:
            self._store(key, value)

    def compute(self, key, fn):
        with self.lock:
            value = fn(self.data.get(key))
            self._store(key, value)
            return value

    def __len__(self) -> int:
        with self.lock:
            return len(self.data)
