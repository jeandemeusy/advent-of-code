from io import TextIOWrapper
from tabnanny import check


def check_line_part1(line: str) -> int:
    ans = 0
    result, num_str = line.split(':')
    result = int(result.strip())
    nums = list(map(lambda x: int(x), num_str.strip().split()))

    for i in range(2 ** (len(nums) - 1)):
        temp = nums[0]
        for j in range(len(nums) - 1):
            if i & (1 << j):
                temp *= nums[j + 1]
            else:
                temp += nums[j + 1]
        if temp == result:
            ans = result
            break

    return ans


def check_line_part2(line: str) -> int:
    return check_line_part1(line)


def part1(f: TextIOWrapper) -> int:
    ans = sum(check_line_part1(line) for line in f)

    return ans


def part2(f: TextIOWrapper) -> int:
    ans = sum(check_line_part2(line) for line in f)

    return ans
