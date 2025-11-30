from io import TextIOWrapper


def part1(f: TextIOWrapper) -> int:
    ans = 0

    for line in f:
        a, b = line.split()
        a, b = "ABC".index(a), "XYZ".index(b)
        ans += b + 1

        if (b - a) % 3 == 0:
            ans += 3
        elif (b - a) % 3 == 1:
            ans += 6

    return ans


def part2(f: TextIOWrapper) -> int:
    ans = 0

    for line in f:
        a, b = line.split()
        a = "ABC".index(a)

        if b == "X":
            ans += (a - 1) % 3 + 1
        elif b == "Y":
            ans += 3
            ans += a + 1
        elif b == "Z":
            ans += 6
            ans += (a + 1) % 3 + 1

    return ans
