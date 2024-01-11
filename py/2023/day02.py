from io import TextIOWrapper


def part1(f: TextIOWrapper) -> int:
    ans = 0

    for line in f:
        id, game = line.split(": ")
        for set in game.split("; "):
            colors = [x.split() for x in set.split(", ")]
            counts = {b: int(a) for a, b in colors}

            if not (
                counts.get("red", 0) <= 12
                and counts.get("green", 0) <= 13
                and counts.get("blue", 0) <= 14
            ):
                break
        else:
            ans += int(id.split()[-1])

    return ans


def part2(f: TextIOWrapper) -> int:
    ans = 0

    for line in f:
        _, game = line.split(": ")
        needed = {"r": 0, "g": 0, "b": 0}

        for set in game.split("; "):
            colors = [x.split() for x in set.split(", ")]
            counts = {b: int(a) for a, b in colors}

            needed["r"] = max(needed["r"], counts.get("red", 0))
            needed["g"] = max(needed["g"], counts.get("green", 0))
            needed["b"] = max(needed["b"], counts.get("blue", 0))

        ans += needed["r"] * needed["g"] * needed["b"]
    return ans
