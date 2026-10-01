import threading
from typing import Callable


class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst: Callable[[], None]) -> None:
        printFirst()
        self.first_done.set()

    def second(self, printSecond: Callable[[], None]) -> None:
        self.first_done.wait()
        printSecond()
        self.second_done.set()

    def third(self, printThird: Callable[[], None]) -> None:
        self.second_done.wait()
        printThird()
