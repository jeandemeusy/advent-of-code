from io import TextIOWrapper


def irange(start: int, end: int) -> range:
    return range(start, end + 1)


def part1(f: TextIOWrapper) -> int:
    ans = 0

    for line in f:
        left, right = line.split(",")
        lrange = set(irange(*map(int, left.split("-"))))
        rrange = set(irange(*map(int, right.split("-"))))

        ans += len(lrange - rrange) == 0 or len(rrange - lrange) == 0

    return ans


def part2(f: TextIOWrapper) -> int:
    ans = 0

    for line in f:
        left, right = line.split(",")
        lrange = set(irange(*map(int, left.split("-"))))
        rrange = set(irange(*map(int, right.split("-"))))

        ans += len(list(lrange & rrange)) > 0

    return ans
