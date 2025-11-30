from io import TextIOWrapper


def part1(f: TextIOWrapper) -> int:
    ans = 0

    llist = []
    rlist = []
    for line in f:
        l, r = line.split()
        llist.append(int(l))
        rlist.append(int(r))

    llist.sort()
    rlist.sort()

    for litem, ritem in zip(llist, rlist):
        ans += abs(litem - ritem)

    return ans


def part2(f: TextIOWrapper) -> int:
    ans = 0

    llist = []
    rlist = {}
    for line in f:
        l, r = line.split()
        llist.append(int(l))

        if int(r) not in rlist:
            rlist[int(r)] = 0
        rlist[int(r)] += 1

    for item in llist:
        if item in rlist:
            ans += (rlist[item]*item)

    return ans
