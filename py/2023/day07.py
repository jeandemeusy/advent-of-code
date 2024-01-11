from collections import Counter
from io import TextIOWrapper
from itertools import product

order = "AKQJT98765432"


def get_score(x):
    match [b for _, b in Counter(x).most_common()]:
        case 5, *_:
            return 1
        case 4, *_:
            return 2
        case 3, 2, *_:
            return 3
        case 3, *_:
            return 4
        case 2, 2, *_:
            return 5
        case 2, *_:
            return 6
        case _:
            return 7


def part1(f: TextIOWrapper) -> int:
    vals = []

    for line in f:
        cards, pts = line.split()
        vals.append((get_score(cards), [order.index(x) for x in cards], int(pts)))

    vals.sort(reverse=True)
    return sum((i + 1) * v[-1] for i, v in enumerate(vals))


def part2(f: TextIOWrapper) -> int:
    order = "AKQT98765432J"
    vals = []

    for line in f:
        cards, pts = line.split()
        score = get_score(cards)
        for subs in product(order[:-1], repeat=cards.count("J")):
            score = min(score, get_score(cards.replace("J", "") + "".join(subs)))
        vals.append((score, [order.index(x) for x in cards], int(pts)))

    vals.sort(reverse=True)
    return sum((i + 1) * v[-1] for i, v in enumerate(vals))
