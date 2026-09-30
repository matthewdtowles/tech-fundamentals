from collections import deque


class Logger:
    WINDOW = 10

    def __init__(self):
        self.next_allowed = {}  # message -> earliest timestamp it may print again
        self.printed = deque()  # (timestamp, message) in arrival order, for eviction

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.printed and self.printed[0][0] + self.WINDOW <= timestamp:
            _, old = self.printed.popleft()
            if self.next_allowed.get(old, 0) <= timestamp:
                del self.next_allowed[old]
        if timestamp < self.next_allowed.get(message, timestamp):
            return False
        self.next_allowed[message] = timestamp + self.WINDOW
        self.printed.append((timestamp, message))
        return True
