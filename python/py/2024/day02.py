from io import TextIOWrapper


def is_safe(report: list[int]) -> bool:
    diffs = [val2-val1 for val1, val2 in zip(report, report[1:])]

    if any(diff > 0 for diff in diffs) and any(diff < 0 for diff in diffs):
        return False

    if min(abs(diff) for diff in diffs) < 1 or max(abs(diff) for diff in diffs) > 3:
        return False

    return True


def part1(f: TextIOWrapper) -> int:
    ans = 0

    for line in f:
        report = [int(val) for val in line.split()]
        ans += is_safe(report)
    return ans


def part2(f: TextIOWrapper) -> int:
    ans = 0

    for line in f:
        report: list[int] = [int(val) for val in line.split()]
        ok = is_safe(report)

        if not ok:
            for i in range(len(report)):
                temp = report.pop(i)
                ok = is_safe(report)
                if ok:
                    break
                report.insert(i, temp)

        ans += ok

    return ans
