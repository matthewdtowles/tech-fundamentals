"""The ordered curriculum. One problem per day. Day numbers come from list order."""
from dataclasses import dataclass

TESTS_MARKER = "# ==== TESTS (do not edit below this line) ===="


@dataclass(frozen=True)
class Day:
    n: int
    slug: str
    title: str
    module: str
    pattern: str
    target: str
    concepts: tuple
    kind: str = "code"  # "code" -> python file with tests, "written" -> markdown reviewed by Claude
    lc: int = None
    lc_slug: str = None
    difficulty: str = None

    @property
    def filename(self):
        return f"day{self.n:02d}_{self.slug}.{'py' if self.kind == 'code' else 'md'}"

    @property
    def url(self):
        return f"https://leetcode.com/problems/{self.lc_slug}/" if self.lc_slug else None


def lc(num, lc_slug, difficulty):
    return dict(lc=num, lc_slug=lc_slug, difficulty=difficulty)


M1 = "1. Hashing & Arrays"
M2 = "2. Two Pointers & Sliding Window"
M3 = "3. Binary Search"
M4 = "4. Linked Lists & Caches"
M5 = "5. Heaps & Scheduling"
M6 = "6. Stacks & Parsing"
M7 = "7. Intervals"
M8 = "8. Trees"
M9 = "9. Graphs"
M10 = "10. Dynamic Programming"
M11 = "11. Rate Limiting & Streams"
M12 = "12. Concurrency"
M13 = "13. Mock Interviews"
M14 = "14. System Design"
M15 = "15. Behavioral & Readiness"

_SPECS = [
    # ---- 1. Hashing & Arrays ----
    dict(slug="two_sum", title="Two Sum", module=M1, pattern="Hash map (complement lookup)",
         target="O(n) time, O(n) space", **lc(1, "two-sum", "Easy"),
         concepts=("Hash map average O(1) get/put vs balanced BST O(log n) — and when ordering makes a tree worth it",
                   "Hash collisions, load factor, resizing: why O(1) is *amortized average*, worst case O(n)",
                   "Trading space for time: brute force O(n^2)/O(1) vs one-pass map O(n)/O(n)",
                   "One-pass trick: check for the complement before inserting the current element")),
    dict(slug="logger_rate_limiter", title="Logger Rate Limiter", module=M1, pattern="Hash map of last-seen timestamps",
         target="O(1) per call; bounded memory is the follow-up", **lc(359, "logger-rate-limiter", "Easy"),
         concepts=("Map message -> next allowed timestamp",
                   "Unbounded growth: a map that never evicts is a memory leak in production",
                   "Eviction options: periodic sweep, queue of (time, msg), two-bucket rotation",
                   "Monotonic timestamps assumption and what breaks if clocks go backwards")),
    # ---- 2. Two Pointers & Sliding Window ----
    dict(slug="longest_substring_no_repeat", title="Longest Substring Without Repeating Characters", module=M2,
         pattern="Variable sliding window + hash map", target="O(n) time, O(min(n, alphabet)) space",
         **lc(3, "longest-substring-without-repeating-characters", "Medium"),
         concepts=("Sliding window template: expand right, shrink left while invalid, record best",
                   "Jumping left pointer using last-seen index map (never move left backwards)",
                   "Each index enters/leaves window once -> O(n)",
                   "Streaming view: the window is a bounded buffer over an unbounded stream")),
    dict(slug="fruit_into_baskets", title="Fruit Into Baskets", module=M2, pattern="Sliding window with at-most-K distinct",
         target="O(n) time, O(1) space", **lc(904, "fruit-into-baskets", "Medium"),
         concepts=("Recognize 'longest subarray with at most K distinct values'",
                   "Window state as a count map; delete keys when count hits 0",
                   "Generalizing K=2 to any K")),
    # ---- 3. Binary Search ----
    dict(slug="binary_search", title="Binary Search", module=M3, pattern="Classic binary search",
         target="O(log n) time, O(1) space", **lc(704, "binary-search", "Easy"),
         concepts=("Invariant-driven binary search: define what lo/hi mean and keep it true",
                   "Closed [lo, hi] vs half-open [lo, hi) loops and their exit conditions",
                   "mid = lo + (hi - lo) // 2 (overflow habit from Java/C)",
                   "Lower bound / upper bound variants (bisect_left, bisect_right)")),
    dict(slug="time_map", title="Time Based Key-Value Store", module=M3, pattern="Hash map + binary search floor",
         target="set O(1), get O(log n), O(n) space", **lc(981, "time-based-key-value-store", "Medium"),
         concepts=("Versioned storage: key -> append-only list of (timestamp, value)",
                   "Timestamps strictly increase per key, so the list stays sorted for free",
                   "Floor search: largest timestamp <= query (bisect_right - 1)",
                   "Production analogs: MVCC, time-series stores, config history")),
    # ---- 4. Linked Lists & Caches ----
    dict(slug="lru_cache", title="LRU Cache", module=M4, pattern="Hash map + doubly linked list",
         target="get O(1), put O(1)", **lc(146, "lru-cache", "Medium"),
         concepts=("Map key -> node for O(1) lookup; DLL for O(1) recency reordering",
                   "Head/tail sentinel nodes remove boundary checks",
                   "Node stores its key so eviction can delete from the map",
                   "OrderedDict does this for you — know both, interviewers usually want the manual version",
                   "TTL extension: store expiry per node, check on get")),
    dict(slug="lfu_cache", title="LFU Cache", module=M4, pattern="Frequency buckets of ordered sets + min-freq pointer",
         target="get O(1), put O(1)", **lc(460, "lfu-cache", "Hard"),
         concepts=("Two maps: key -> (value, freq) and freq -> ordered keys (LRU tiebreak within a freq)",
                   "min_freq pointer: only ever increments by 1 on touch, resets to 1 on insert",
                   "Why a heap would be O(log n) and is not acceptable",
                   "LFU vs LRU trade-offs: frequency pollution from old hot keys")),
    # ---- 5. Heaps & Scheduling ----
    dict(slug="top_k_frequent", title="Top K Frequent Elements", module=M5, pattern="Count + heap or bucket sort",
         target="O(n log k) with heap, or O(n) with bucket sort", **lc(347, "top-k-frequent-elements", "Medium"),
         concepts=("Counter to get frequencies",
                   "Heap of size k over (freq, value)",
                   "Bucket sort by frequency: index = count, max index = n",
                   "Heavy-hitters at scale: Count-Min Sketch as the streaming approximation")),
    dict(slug="merge_k_lists", title="Merge k Sorted Lists", module=M5, pattern="K-way merge with a heap",
         target="O(N log k) time, O(k) space", **lc(23, "merge-k-sorted-lists", "Hard"),
         concepts=("Heap holds one head per list; pop smallest, push its next",
                   "Tie-breaking: push (val, index, node) so nodes are never compared",
                   "Divide and conquer pairwise merge is also O(N log k)",
                   "Production: merging sorted log segments / SSTables / external sort")),
    # ---- 6. Stacks & Parsing ----
    dict(slug="daily_temperatures", title="Daily Temperatures", module=M6, pattern="Monotonic decreasing stack",
         target="O(n) time, O(n) space", **lc(739, "daily-temperatures", "Medium"),
         concepts=("Monotonic stack: store indices of unresolved items",
                   "When a bigger value arrives, it resolves everything smaller on the stack",
                   "Each index is pushed and popped once -> O(n)",
                   "Next greater / next smaller element family")),
    dict(slug="largest_rectangle", title="Largest Rectangle in Histogram", module=M6, pattern="Monotonic increasing stack",
         target="O(n) time, O(n) space", **lc(84, "largest-rectangle-in-histogram", "Hard"),
         concepts=("For each bar, width extends to the nearest smaller bar on each side",
                   "Popping a bar means its right boundary is found; the new stack top is its left boundary",
                   "Sentinel 0 at the end flushes the stack")),
    dict(slug="uncommon_words", title="Uncommon Words from Two Sentences", module=M6, pattern="Tokenize + count",
         target="O(m + n) time and space", **lc(884, "uncommon-words-from-two-sentences", "Easy"),
         concepts=("Reframe: uncommon = appears exactly once across both sentences",
                   "str.split() tokenization and its whitespace behavior",
                   "Counter over the concatenated token stream")),
    dict(slug="text_justification", title="Text Justification", module=M6, pattern="Greedy line packing + careful formatting",
         target="O(total characters) time", **lc(68, "text-justification", "Hard"),
         concepts=("Greedy: pack as many words as fit (words + minimum single spaces <= width)",
                   "Distribute spaces: base = gaps // slots, extra go to the leftmost slots",
                   "Special cases: last line and single-word lines are left-justified",
                   "Write helper functions; boundary logic is the whole problem")),
    # ---- 7. Intervals ----
    dict(slug="merge_intervals", title="Merge Intervals", module=M7, pattern="Sort by start + sweep",
         target="O(n log n) time, O(n) space", **lc(56, "merge-intervals", "Medium"),
         concepts=("Sorting by start means overlaps can only happen with the last merged interval",
                   "Overlap test: next.start <= last.end (touching counts here)",
                   "Merged end = max(last.end, next.end) — a contained interval must not shrink it")),
    dict(slug="insert_interval", title="Insert Interval", module=M7, pattern="Three-phase linear scan",
         target="O(n) time, O(n) space", **lc(57, "insert-interval", "Medium"),
         concepts=("Input is already sorted: no need to sort again",
                   "Phase 1: intervals ending before new start; phase 2: merge overlaps; phase 3: rest",
                   "Why O(n) beats re-sorting")),
    # ---- 8. Trees ----
    dict(slug="level_order", title="Binary Tree Level Order Traversal", module=M8, pattern="BFS with level sizing",
         target="O(n) time, O(w) space (w = max width)", **lc(102, "binary-tree-level-order-traversal", "Medium"),
         concepts=("collections.deque for O(1) popleft (list.pop(0) is O(n))",
                   "Snapshot len(queue) at the start of each level",
                   "BFS vs DFS memory profile: width vs height")),
    dict(slug="validate_bst", title="Validate Binary Search Tree", module=M8, pattern="DFS with bounds",
         target="O(n) time, O(h) space", **lc(98, "validate-binary-search-tree", "Medium"),
         concepts=("BST property is global, not just parent/child",
                   "Pass (low, high) bounds down the recursion",
                   "In-order traversal of a BST is strictly increasing — alternative check")),
    # ---- 9. Graphs ----
    dict(slug="number_of_islands", title="Number of Islands", module=M9, pattern="Grid DFS/BFS flood fill",
         target="O(m * n) time, O(m * n) space worst case", **lc(200, "number-of-islands", "Medium"),
         concepts=("Graph representations: adjacency list, matrix, implicit grid",
                   "Flood fill marks a whole component per outer-loop hit",
                   "Recursion depth limits in Python -> prefer iterative BFS for big grids")),
    dict(slug="course_schedule", title="Course Schedule", module=M9, pattern="Cycle detection via Kahn's algorithm",
         target="O(V + E) time and space", **lc(207, "course-schedule", "Medium"),
         concepts=("Build systems as DAGs: an edge means 'must happen before'",
                   "Kahn's: indegree array + queue of zero-indegree nodes",
                   "If processed count < V, there is a cycle",
                   "DFS three-color (white/gray/black) alternative")),
    dict(slug="course_schedule_ii", title="Course Schedule II", module=M9, pattern="Topological sort (Kahn's)",
         target="O(V + E) time and space", **lc(210, "course-schedule-ii", "Medium"),
         concepts=("The order nodes leave the queue IS a valid topological order",
                   "Multiple valid orders exist — tests must accept any",
                   "Return [] on cycle")),
    dict(slug="alien_dictionary", title="Alien Dictionary", module=M9, pattern="Graph construction + topo sort",
         target="O(C) time (C = total characters), O(1) space for 26 letters", **lc(269, "alien-dictionary", "Hard"),
         concepts=("Derive edges only from the FIRST differing character of adjacent words",
                   "Invalid input: a word followed by its own prefix (e.g. 'abc' before 'ab')",
                   "Include every letter as a node even with no edges",
                   "Cycle -> return empty string")),
    # ---- 10. Dynamic Programming ----
    dict(slug="coin_change", title="Coin Change", module=M10, pattern="Unbounded knapsack DP",
         target="O(amount * coins) time, O(amount) space", **lc(322, "coin-change", "Medium"),
         concepts=("DP basics: overlapping subproblems + optimal substructure; memoization vs bottom-up table",
                   "dp[a] = min over coins of dp[a - c] + 1",
                   "Why greedy fails (coins [1,3,4], amount 6)",
                   "Infinity sentinel for unreachable amounts",
                   "BFS view: shortest path in amount-space")),
    # ---- 11. Rate Limiting & Streams ----
    dict(slug="token_bucket", title="Token Bucket Rate Limiter", module=M11, pattern="Lazy refill arithmetic",
         target="O(1) per call, O(1) space", difficulty="Medium",
         concepts=("Fixed window vs sliding log vs sliding window counter vs token bucket vs leaky bucket",
                   "Token bucket allows bursts up to capacity, then sustains refill rate",
                   "Lazy refill on each call: tokens = min(cap, tokens + elapsed * rate)",
                   "Inject a clock for testability (hexagonal: time is a port)")),
    dict(slug="log_aggregation", title="Log Stream Aggregation", module=M11, pattern="Streaming parse + bucketed counters",
         target="O(lines) time, O(minutes + distinct codes) memory — never load the whole file", difficulty="Medium",
         concepts=("Stream line-by-line with a file iterator; never readlines() a multi-GB file",
                   "Regex parsing, skipping malformed lines",
                   "Truncate timestamps to minute buckets for windowed error rates",
                   "Top-K via Counter.most_common / heapq.nlargest")),
    # ---- 12. Concurrency ----
    dict(slug="print_in_order", title="Print in Order", module=M12, pattern="Events / barriers between threads",
         target="No busy-waiting; each thread blocks until its turn", **lc(1114, "print-in-order", "Easy"),
         concepts=("Race conditions, critical sections, happens-before",
                   "Python GIL: prevents parallel bytecode, NOT races between threads",
                   "threading.Event, Lock, Condition, Semaphore — what each is for",
                   "Java map: CountDownLatch, ReentrantLock, Condition, Semaphore",
                   "ReadWriteLock for read-heavy state; Atomic* (CAS) when a single variable needs no lock")),
    dict(slug="foobar_alternately", title="Print FooBar Alternately", module=M12, pattern="Paired semaphores",
         target="Strict alternation, no busy-waiting", **lc(1115, "print-foobar-alternately", "Medium"),
         concepts=("Semaphores as permits: acquire decrements, release increments",
                   "Ping-pong: foo releases bar's semaphore and vice versa",
                   "Condition variable alternative: always wait in a while loop (spurious wakeups)")),
    dict(slug="bounded_blocking_queue", title="Design Bounded Blocking Queue", module=M12, pattern="Condition variables (producer-consumer)",
         target="enqueue/dequeue O(1), block instead of spin", **lc(1188, "design-bounded-blocking-queue", "Medium"),
         concepts=("Producer-consumer with two conditions: not_full and not_empty sharing one lock",
                   "while (not predicate): wait()  — never 'if'",
                   "Backpressure: bounded queues protect memory",
                   "Java: ArrayBlockingQueue / LinkedBlockingQueue")),
    dict(slug="ring_buffer", title="Thread-Safe Ring Buffer", module=M12, pattern="Circular array with head/count",
         target="put/get O(1), fixed memory", difficulty="Medium",
         concepts=("Circular indexing: (head + count) % capacity",
                   "Full vs empty disambiguation (count field or one wasted slot)",
                   "Lock-based vs lock-free (CAS, LMAX Disruptor) trade-offs",
                   "Cache lines and false sharing (conceptual)")),
    dict(slug="web_crawler_mt", title="Web Crawler Multithreaded", module=M12, pattern="Thread pool + thread-safe visited set",
         target="Concurrent fetches; O(V + E) total work", **lc(1242, "web-crawler-multithreaded", "Medium"),
         concepts=("ThreadPoolExecutor and futures",
                   "Check-and-add to visited must be atomic (lock) to avoid duplicate work",
                   "Termination: track in-flight tasks, stop when none remain",
                   "I/O-bound work benefits from threads even with the GIL")),
    dict(slug="worker_pool", title="Worker Pool with Graceful Shutdown", module=M12, pattern="Threads + queue + poison pills",
         target="Submit O(1); shutdown drains queued work, then joins", difficulty="Medium",
         concepts=("Fixed pool of worker threads pulling from a shared queue",
                   "Graceful shutdown: stop accepting, drain, send one poison pill per worker, join",
                   "Error isolation: one failing task must not kill a worker",
                   "Java: ExecutorService.shutdown() vs shutdownNow(), awaitTermination")),
    dict(slug="mt_log_processor", title="Multithreaded Log Pipeline", module=M12, pattern="Producer -> workers -> aggregator pipeline",
         target="Correct totals under concurrency; bounded memory via bounded queue", difficulty="Medium",
         concepts=("Pipeline stages connected by bounded queues",
                   "Per-worker local counters merged at the end beat a shared locked counter",
                   "Sentinels to signal end-of-stream through each stage")),
    # ---- 13. Mock Interviews ----
    dict(slug="mock_lru", title="Mock: LRU Cache (40-minute timer)", module=M13, pattern="Live coding drill",
         target="get O(1), put O(1); finish in 40 minutes", **lc(146, "lru-cache", "Medium"),
         concepts=("Step 1 (5 min): clarify constraints out loud",
                   "Step 2 (5 min): brute force vs optimal, state complexities",
                   "Step 3 (20 min): write clean code",
                   "Step 4 (10 min): dry-run tests and edge cases")),
    dict(slug="mock_course_schedule_ii", title="Mock: Course Schedule II (narrated)", module=M13, pattern="Live coding drill",
         target="O(V + E) time and space; finish in 35 minutes", **lc(210, "course-schedule-ii", "Medium"),
         concepts=("Narrate trade-offs: Kahn's vs DFS, O(V + E) time/space",
                   "State assumptions about input validity",
                   "Test with a cycle, a disconnected graph, and zero prerequisites")),
    # ---- 14. System Design ----
    dict(slug="design_logging_metrics", title="Design a Distributed Logging & Metrics System", module=M14, kind="written",
         pattern="System design", target="45-minute design covering requirements -> API -> data -> scale -> failures", difficulty="Hard",
         concepts=("Framework: requirements, estimates, API, data model, high-level design, deep dives, trade-offs",
                   "Agents -> buffer (Kafka) -> stream processors -> hot store / cold store",
                   "At-least-once vs exactly-once; idempotency keys; transactional outbox",
                   "Cardinality explosion in metrics labels; downsampling and retention tiers")),
    dict(slug="design_event_streaming_sdk", title="Design a High-Throughput Event Streaming SDK", module=M14, kind="written",
         pattern="System design", target="Client SDK design: batching, retries, ordering, backpressure", difficulty="Hard",
         concepts=("Partitioning strategies: key hash, round robin, sticky; ordering is per partition",
                   "Batching + linger time vs latency; compression",
                   "Retries with backoff + jitter; idempotent producer; dead-letter queues",
                   "Backpressure: bounded in-memory buffer, block vs drop policies")),
    dict(slug="design_video_streaming", title="Design a Video Streaming Platform", module=M14, kind="written",
         pattern="System design", target="Netflix-scale upload -> transcode -> CDN -> adaptive playback", difficulty="Hard",
         concepts=("Transcoding pipeline: chunking, parallel encode, multiple bitrates",
                   "Adaptive bitrate streaming (HLS/DASH) and manifests",
                   "CDN / Open Connect: pre-positioning popular content at the edge",
                   "Resilience: chaos engineering, regional failover, bulkheads, circuit breakers")),
    # ---- 15. Behavioral & Readiness ----
    dict(slug="story_architecture", title="STAR Story: Modernizing Core Architecture", module=M15, kind="written",
         pattern="Behavioral (STAR)", target="A 2-3 minute story with measurable results", difficulty="Medium",
         concepts=("STAR: Situation, Task, Action, Result — Action is ~60% of the story",
                   "Say 'I', not 'we', for your actions",
                   "Quantify results (latency, cost, loss rate, time saved)",
                   "Prepare follow-ups: what would you do differently?")),
    dict(slug="story_production_incident", title="STAR Story: Resolving a Major Production Issue", module=M15, kind="written",
         pattern="Behavioral (STAR)", target="A 2-3 minute story showing ownership and debugging method", difficulty="Medium",
         concepts=("Show your debugging method, not just the fix",
                   "Blameless framing; what you changed to prevent recurrence",
                   "Communication during the incident")),
    dict(slug="story_leadership", title="STAR Story: Leading Cross-Functional Technical Decisions", module=M15, kind="written",
         pattern="Behavioral (STAR)", target="A 2-3 minute story showing influence without authority", difficulty="Medium",
         concepts=("Influence without authority: data, prototypes, RFCs",
                   "Disagree and commit; handling pushback",
                   "Adoption metrics as results")),
    dict(slug="netflix_culture", title="Culture Fit: Freedom & Responsibility", module=M15, kind="written",
         pattern="Behavioral (values)", target="Stories mapped to candor, judgment, and context-not-control", difficulty="Medium",
         concepts=("Netflix culture memo: freedom & responsibility, context not control, keeper test",
                   "Candid feedback: a story of giving and receiving hard feedback",
                   "Judgment: a decision you made with incomplete information",
                   "Highly aligned, loosely coupled teams")),
    dict(slug="pattern_review", title="Final Polish: Pattern Recognition Sheet", module=M15, kind="written",
         pattern="Review", target="One-page sheet: signal -> pattern -> complexity for 15+ patterns", difficulty="Medium",
         concepts=("Problem signals -> pattern (e.g. 'sorted + target' -> two pointers / binary search)",
                   "Hash maps, sliding windows, heaps, monotonic stacks, graphs, DP, locks",
                   "Complexity of each pattern from memory")),
]

DAYS = tuple(Day(n=i + 1, **spec) for i, spec in enumerate(_SPECS))


def get(n):
    if not 1 <= n <= len(DAYS):
        raise ValueError(f"Day must be between 1 and {len(DAYS)}.")
    return DAYS[n - 1]
