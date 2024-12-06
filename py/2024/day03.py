import re
from io import TextIOWrapper


def part1(f: TextIOWrapper) -> int:
    ans = 0

    mults = re.findall(r'mul\(\d+,\d+\)', f.read())

    for i in mults:
        n1, n2 = re.findall(r'\d+', i)
        ans += int(n1) * int(n2)

    return ans


def part2(f: TextIOWrapper) -> int:
    ans = 0

    pattern = re.compile(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)')
    instructions = re.findall(pattern, f.read())

    enable = True
    for i in instructions:
        if i == 'do()':
            enable = True
        elif i == 'don\'t()':
            enable = False
        else:
            if enable:
                n1, n2 = re.findall(r'\d+', i)
                ans += int(n1) * int(n2)

    return ans
