from io import TextIOWrapper


def deserialize(lines: list[str], sep=',') -> list:
    return [list(map(lambda x: int(x), line.strip().split(sep)))
            for line in lines]


def part1(f: TextIOWrapper) -> int:
    ans = 0

    lines = f.readlines()
    # find line which is empty
    separator_index = None
    for i, line in enumerate(lines):
        if line == "\n":
            separator_index = i
            break

    if separator_index is None:
        return 0

    rules = deserialize(lines[:separator_index], "|")
    updates = deserialize(lines[separator_index+1:])

    print(f"{rules=}")
    print(f"{updates=}")

    return ans


def part2(f: TextIOWrapper) -> int:
    ans = 0

    return ans
