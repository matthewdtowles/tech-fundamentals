import threading
from collections import deque


class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = deque()
        lock = threading.Lock()
        self.not_full = threading.Condition(lock)
        self.not_empty = threading.Condition(lock)

    def enqueue(self, element: int) -> None:
        with self.not_full:
            while len(self.items) == self.capacity:
                self.not_full.wait()
            self.items.append(element)
            self.not_empty.notify()

    def dequeue(self) -> int:
        with self.not_empty:
            while not self.items:
                self.not_empty.wait()
            element = self.items.popleft()
            self.not_full.notify()
            return element

    def size(self) -> int:
        with self.not_full:
            return len(self.items)
