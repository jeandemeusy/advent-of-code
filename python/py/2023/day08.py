import math
from io import TextIOWrapper
from itertools import cycle

corrs = {"L": 0, "R": 1}


def part1(f: TextIOWrapper) -> int:
    path, maps = f.read().split("\n\n")
    maps = [x.split(" = ") for x in maps.splitlines()]
    maps = {a: b[1:-1].split(", ") for a, b in maps}

    curr = "AAA"
    for count, d in enumerate(cycle(path), start=1):
        curr = maps[curr][d == "R"]
        if curr == "ZZZ":
            return count


def part2(f: TextIOWrapper) -> int:
    path, maps = f.read().split("\n\n")
    maps = [x.split(" = ") for x in maps.splitlines()]
    maps = {a: b[1:-1].split(", ") for a, b in maps}

    ans = []

    for curr in maps:
        if not curr.endswith("A"):
            continue
        visited = set()
        for count, (idx, d) in enumerate(cycle(enumerate(path)), start=1):
            prev, curr = curr, maps[curr][d == "R"]
            visited.add((curr, idx))
            if prev.endswith("Z") and (curr, idx) in visited:
                ans.append(count - 1)
                break

    return math.lcm(*ans)
