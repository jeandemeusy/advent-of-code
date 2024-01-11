from io import TextIOWrapper


def find_start(line: str, size: int) -> int:
    idx = 0
    while len(set(line[idx : idx + size])) != size:
        idx += 1
    return idx + size


def part1(f: TextIOWrapper) -> int:
    return find_start(f.readline(), 4)


def part2(f: TextIOWrapper) -> int:
    return find_start(f.readline(), 14)
