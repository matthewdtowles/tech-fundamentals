import random


class RandomizedSet:
    def __init__(self):
        self.values = []
        self.index = {}  # value -> position in self.values

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        i, last = self.index.pop(val), self.values.pop()
        if i < len(self.values):
            self.values[i] = last
            self.index[last] = i
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
