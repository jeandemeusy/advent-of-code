from io import TextIOWrapper


def part1(f: TextIOWrapper) -> int:
    ans = 0

    for card in f:
        winnings, candidates = map(set, map(str.split, card.split("|")))
        count = len(winnings & candidates)
        ans += 2 ** (count - 1) if count > 0 else 0
    return ans


def part2(f: TextIOWrapper) -> int:
    data = f.read().splitlines()
    card_count = [1] * len(data)

    for id, count in enumerate(card_count):
        winnings, candidates = map(set, map(str.split, data[id].split("|")))
        for i in range(len(winnings & candidates)):
            card_count[id + i + 1] += count

    return sum(card_count)
