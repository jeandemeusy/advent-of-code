from io import TextIOWrapper


def next_number(numbers: list[int]) -> int:
    if all(num == 0 for num in numbers):
        return 0

    diffs = [a - b for a, b in zip(numbers[1:], numbers[:-1])]

    return numbers[-1] + next_number(diffs)


def part1(f: TextIOWrapper) -> int:
    return sum(next_number([int(x) for x in line.split()]) for line in f)


def part2(f: TextIOWrapper) -> int:
    return sum(next_number([int(x) for x in line.split()[::-1]]) for line in f)
