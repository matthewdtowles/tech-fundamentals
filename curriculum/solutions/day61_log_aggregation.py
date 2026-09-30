import heapq
import re
from collections import Counter, defaultdict

LINE = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}):\d{2} \[(\w+)\] ([\w-]+): (.*)$")
CODE = re.compile(r"^(E\d+)\b")


def analyze(path: str, top_n: int = 5) -> dict:
    totals, errors, codes = defaultdict(int), defaultdict(int), Counter()
    malformed = 0
    with open(path) as f:
        for line in f:
            match = LINE.match(line.rstrip("\n"))
            if not match:
                malformed += 1
                continue
            minute, level, _, message = match.groups()
            totals[minute] += 1
            if level == "ERROR":
                errors[minute] += 1
                code = CODE.match(message)
                if code:
                    codes[code.group(1)] += 1
    return {
        "error_rate": {m: errors[m] / totals[m] for m in totals},
        "top_errors": heapq.nsmallest(top_n, codes.items(), key=lambda kv: (-kv[1], kv[0])),
        "malformed": malformed,
    }
