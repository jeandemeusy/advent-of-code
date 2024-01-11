import re
from collections import defaultdict
from io import TextIOWrapper


def part1(f: TextIOWrapper) -> int:
    data = f.read().splitlines()
    ans = 0
    for i, line in enumerate(data):
        for m in re.finditer(r"\d+", line):
            idxs = [(i, m.start() - 1), (i, m.end())]
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
            count = sum(
                0 <= a < len(data) and 0 <= b < len(data[a]) and data[a][b] != "."
                for a, b in idxs
            )
            if count > 0:
                ans += int(m.group())
    return ans


def part2(f: TextIOWrapper) -> int:
    data = f.read().splitlines()
    adj = defaultdict(list)
    for i, line in enumerate(data):
        for m in re.finditer(r"\d+", line):
            idxs = [(i, m.start() - 1), (i, m.end())]
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
            for a, b in idxs:
                if 0 <= a < len(data) and 0 <= b < len(data[a]) and data[a][b] == "*":
                    adj[a, b].append(m.group())
    return sum(int(x[0]) * int(x[1]) for x in adj.values() if len(x) == 2)
