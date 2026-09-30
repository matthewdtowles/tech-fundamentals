import queue
import threading

_STOP = object()  # poison pill


class WorkerPool:
    def __init__(self, num_workers: int):
        self.tasks = queue.Queue()
        self.accepting = True
        self.lock = threading.Lock()
        self.workers = [threading.Thread(target=self._work, daemon=True) for _ in range(num_workers)]
        for w in self.workers:
            w.start()

    def _work(self):
        while True:
            task = self.tasks.get()
            if task is _STOP:
                return
            fn, args = task
            try:
                fn(*args)
            except Exception:
                pass  # a real pool would log this

    def submit(self, fn, *args) -> None:
        with self.lock:
            if not self.accepting:
                raise RuntimeError("pool is shut down")
            self.tasks.put((fn, args))

    def shutdown(self) -> None:
        with self.lock:
            self.accepting = False
        for _ in self.workers:  # FIFO: pills land after every queued task
            self.tasks.put(_STOP)
        for w in self.workers:
            w.join()
