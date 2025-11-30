from io import TextIOWrapper

PRIO = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part1(f: TextIOWrapper) -> int:
    ans = 0

    for line in f:
        m = len(line) // 2
        c = set(line[:m]) & set(line[m:])

        ans += PRIO.index(next(iter(c)))

    return ans


def part2(f: TextIOWrapper) -> int:
    data = f.read().splitlines()
    ans = 0

    data = iter(data)
    while True:
        try:
            a, b, c = next(data), next(data), next(data)
        except StopIteration:
            break

        d = set(a) & set(b) & set(c)
        ans += PRIO.index(next(iter(d)))

    return ans
