from io import TextIOWrapper


def compute_num(num: str) -> list[str]:
    num = num.lstrip("0")
    len_num: int = len(num)

    if len_num == 0:
        return ["1"]

    if len_num % 2 == 0:
        return [num[:len_num//2], num[len_num//2:]]

    return [str(int(num)*2024)]


def part1(f: TextIOWrapper) -> int:
    ans = 0
    steps = 25
    cache: dict = {}

    numbers = f.readline().split()

    for _ in range(steps):
        new_numbers = []

        for num in numbers:
            if num not in cache:
                cache[num] = compute_num(num)

            new_numbers.extend(cache[num])

        numbers = new_numbers

    ans = len(numbers)
    return ans


def part2(f: TextIOWrapper) -> int:
    return part1(f)
