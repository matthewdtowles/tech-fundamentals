import threading


class RingBuffer:
    def __init__(self, capacity: int):
        self.slots = [None] * capacity
        self.head = 0   # index of the front item
        self.count = 0  # disambiguates full vs empty
        self.lock = threading.Lock()

    def offer(self, item) -> bool:
        with self.lock:
            if self.count == len(self.slots):
                return False
            self.slots[(self.head + self.count) % len(self.slots)] = item
            self.count += 1
            return True

    def poll(self):
        with self.lock:
            if self.count == 0:
                return None
            item, self.slots[self.head] = self.slots[self.head], None
            self.head = (self.head + 1) % len(self.slots)
            self.count -= 1
            return item

    def __len__(self) -> int:
        with self.lock:
            return self.count
