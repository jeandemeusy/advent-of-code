from io import TextIOWrapper
from math import inf

nums = "0 zero 1 one 2 two 3 three 4 four 5 five 6 six 7 seven 8 eight 9 nine".split()


def part1(f: TextIOWrapper) -> int:
    data = f.read().splitlines()
    ans = 0
    for line in data:
        first = next((x for x in line if x.isdigit()), 0)
        last = next((x for x in line[::-1] if x.isdigit()), 0)
        ans += int(first) * 10 + int(last)
    return ans


def part2(f: TextIOWrapper) -> int:
    ans = 0
    for line in f:
        first = min(nums, key=lambda x: line.index(x) if x in line else inf)
        last = min(nums, key=lambda x: line[::-1].index(x[::-1]) if x in line else inf)
        ans += nums.index(first) // 2 * 10 + nums.index(last) // 2
    return ans
