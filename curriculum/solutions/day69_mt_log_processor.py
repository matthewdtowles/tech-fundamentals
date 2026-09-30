import queue
import threading
from collections import Counter

_END = object()


def process_logs(lines, parse, num_workers=4, queue_size=1000) -> Counter:
    work = queue.Queue(maxsize=queue_size)
    partials = [Counter() for _ in range(num_workers)]

    def reader():
        for line in lines:
            work.put(line)  # blocks when full: backpressure
        for _ in range(num_workers):
            work.put(_END)

    def worker(counts):
        while True:
            line = work.get()
            if line is _END:
                return
            key = parse(line)
            if key is not None:
                counts[key] += 1

    threads = [threading.Thread(target=reader)] + [threading.Thread(target=worker, args=(c,)) for c in partials]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return sum(partials, Counter())
