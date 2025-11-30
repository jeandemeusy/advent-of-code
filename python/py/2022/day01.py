from io import TextIOWrapper


def part1(f: TextIOWrapper) -> int:
    ans, temp = [], 0

    for line in f:
        if line == "":
            ans.append(temp)
            temp = 0
            continue

        temp += int(line)

    return max(ans)


def part2(f: TextIOWrapper) -> int:
    ans, temp = [], 0

    for line in f:
        if line == "":
            ans.append(temp)
            temp = 0
            continue

        temp += int(line)

    ans.append(temp)
    ans.sort()

    return sum(ans[-3:])
