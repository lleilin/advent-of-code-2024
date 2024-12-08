from collections import defaultdict

def part1(path):
    mp = defaultdict(list)
    with open(path) as file:
        for i, row in enumerate(file):
            for j, val in enumerate(row.rstrip()):
                if val == ".":
                    continue
                mp[val].append((i, j))
    m, n = i + 1, j + 1

    return part1_helper(mp, m, n)


def part1_helper(mp, m, n):
    st = set()

    for arr in mp.values():
        for idx, (i1, j1) in enumerate(arr):
            for i2, j2 in arr[idx + 1 :]:
                di, dj = i1 - i2, j1 - j2
                i3, j3 = i1 + di, j1 + dj
                i4, j4 = i2 - di, j2 - dj
                if 0 <= i3 < m and 0 <= j3 < n:
                    st.add((i3, j3))
                if 0 <= i4 < m and 0 <= j4 < n:
                    st.add((i4, j4))
    return len(st)


def part2(path):
    mp = defaultdict(list)
    with open(path) as file:
        for i, row in enumerate(file):
            for j, val in enumerate(row.rstrip()):
                if val == ".":
                    continue
                mp[val].append((i, j))
    m, n = i + 1, j + 1

    return part2_helper(mp, m, n)


def part2_helper(mp, m, n):
    st = set()

    for arr in mp.values():
        for idx, (i1, j1) in enumerate(arr):
            for i2, j2 in arr[idx + 1 :]:
                di, dj = i1 - i2, j1 - j2
                i3, j3 = i1,j1
                i4, j4 = i1,j1
                while 0 <= i3 < m and 0 <= j3 < n:
                    st.add((i3, j3))
                    i3 += di
                    j3 += dj
                while 0 <= i4 < m and 0 <= j4 < n:
                    st.add((i4, j4))
                    i4 -= di
                    j4 -= dj
    # print(sorted(st))
    return len(st)


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
