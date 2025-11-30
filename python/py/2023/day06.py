import math
from io import TextIOWrapper


def part1(f: TextIOWrapper) -> int:
    ans = 1
    races = [map(int, line.split()[1:]) for line in f]

    for time, dist in zip(*races):
        ans *= sum((time - hold) * hold >= dist for hold in range(time))

    return ans


def part2(f: TextIOWrapper) -> int:
    time, dist = [int(line.replace(" ", "").split(":")[1]) for line in f]
    a = (time - math.sqrt(time**2 - 4 * dist)) / 2
    b = (time + math.sqrt(time**2 - 4 * dist)) / 2
    return math.floor(b) - math.ceil(a) + 1
