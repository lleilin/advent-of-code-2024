from collections import defaultdict


def part1(path):
    mp = defaultdict(int)
    with open(path) as file:
        line = file.readline()
        arr = line.split()
        arr = [int(i) for i in arr]
        for i in arr:
            mp[i]+=1

    for i in range(1, 26):
        mp = part1_helper(mp)

    return sum(mp.values())

def part1_helper(mp):
    new_mp = defaultdict(int)
    for k, v in mp.items():
        s = str(k)
        if k == 0:
            new_mp[1] += v
        elif len(s) % 2 == 0:
            for m in int(s[: len(s) // 2]), int(s[len(s) // 2 :]):
                new_mp[m] += v
        else:
            new_mp[2024 * k] += v
    return new_mp


def part2(path):
    mp = defaultdict(int)
    with open(path) as file:
        line = file.readline()
        arr = line.split()
        arr = [int(i) for i in arr]
        for i in arr:
            mp[i]+=1

    for i in range(1, 76):
        mp = part1_helper(mp)

    return sum(mp.values())


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
