"""
Build a fixed-size worker pool with graceful shutdown — WITHOUT
concurrent.futures (that's what you're re-implementing).

  WorkerPool(num_workers)      start num_workers threads that pull tasks from a shared queue
  submit(fn, *args) -> None    enqueue a task; raise RuntimeError after shutdown() was called
  shutdown() -> None           stop accepting new tasks, let workers finish EVERY task
                               already queued, then join all worker threads before returning

Requirements:
  - A task that raises must not kill its worker (catch and log/ignore).
  - After shutdown() returns, no worker threads are alive.
  - Use queue.Queue + threading.Thread. Poison pills (one sentinel per worker)
    are the classic way to stop workers.

Discuss first: Java's ExecutorService.shutdown() vs shutdownNow() and
awaitTermination(); why one sentinel per worker; what "graceful" means.
"""
import queue
import threading


class WorkerPool:
    def __init__(self, num_workers: int):
        pass

    def submit(self, fn, *args) -> None:
        raise NotImplementedError

    def shutdown(self) -> None:
        raise NotImplementedError


# ==== TESTS (do not edit below this line) ====
import time
import unittest


class TestWorkerPool(unittest.TestCase):
    def test_runs_all_tasks(self):
        pool, results, lock = WorkerPool(4), [], threading.Lock()

        def task(x):
            with lock:
                results.append(x * x)

        for i in range(100):
            pool.submit(task, i)
        pool.shutdown()
        self.assertEqual(sorted(results), [i * i for i in range(100)])

    def test_runs_in_parallel(self):
        pool = WorkerPool(4)
        start = time.perf_counter()
        for _ in range(8):
            pool.submit(time.sleep, 0.1)
        pool.shutdown()
        self.assertLess(time.perf_counter() - start, 0.5, "4 workers x 8 tasks of 0.1s should take ~0.2s")

    def test_shutdown_drains_queue(self):
        pool, done = WorkerPool(2), []
        for i in range(20):
            pool.submit(lambda i=i: (time.sleep(0.01), done.append(i)))
        pool.shutdown()
        self.assertEqual(len(done), 20, "shutdown must finish queued work")

    def test_submit_after_shutdown_raises(self):
        pool = WorkerPool(1)
        pool.shutdown()
        with self.assertRaises(RuntimeError):
            pool.submit(print, "too late")

    def test_failing_task_does_not_kill_worker(self):
        pool, done = WorkerPool(1), []
        pool.submit(lambda: 1 / 0)
        pool.submit(done.append, "still alive")
        pool.shutdown()
        self.assertEqual(done, ["still alive"])

    def test_no_threads_left_behind(self):
        before = threading.active_count()
        pool = WorkerPool(5)
        self.assertEqual(threading.active_count(), before + 5)
        pool.shutdown()
        self.assertEqual(threading.active_count(), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
