from collections import defaultdict

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def part1(path):
    grid = []
    with open(path) as file:
        for row in file.readlines():
            grid.append(row.rstrip())

    m, n = len(grid), len(grid[0])

    mp = defaultdict(set)

    def search(idx, val, i, j):
        if (
            i < 0
            or i >= m
            or j < 0
            or j >= n
            or visited[i][j]
            or grid[i][j] != val
        ):
            return
        mp[idx].add((i, j))
        visited[i][j] = True
        for di, dj in DIRECTIONS:
            search(idx, val, i + di, j + dj)

    visited = [[False for _ in range(n)] for _ in range(m)]
    count = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                continue
            search(count, grid[i][j], i, j)
            count += 1

    ans = 0
    for st in mp.values():
        perimeter = 0
        for i, j in st:
            for di, dj in DIRECTIONS:
                if (
                    0 <= i + di < m
                    and 0 <= j + dj < n
                    and (i + di, j + dj) in st
                ):
                    continue
                perimeter += 1
        ans += len(st) * perimeter
    return ans


def part2(path):
    grid = []
    with open(path) as file:
        for row in file.readlines():
            grid.append(row.rstrip())

    m, n = len(grid), len(grid[0])

    mp = defaultdict(set)

    def search(idx, val, i, j):
        if (
            i < 0
            or i >= m
            or j < 0
            or j >= n
            or visited[i][j]
            or grid[i][j] != val
        ):
            return
        mp[idx].add((i, j))
        visited[i][j] = True
        for di, dj in DIRECTIONS:
            search(idx, val, i + di, j + dj)

    visited = [[False for _ in range(n)] for _ in range(m)]
    count = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j]:
                continue
            search(count, grid[i][j], i, j)
            count += 1

    def count_sides(st):

        ans = 0
        for i, j in st:
            for (di,dj) in [(1,1),(-1,-1),(1,-1),(-1,1)]:
                if (i + di, j) in st and (i, j + dj) in st and (i + di,j + dj) not in st:
                    # print(i,j)
                    ans += 1
                if (i+di,j) not in st and (i,j+dj) not in st:
                    ans += 1
                    
        return ans

    ans = 0
    for st in mp.values():
        sides = count_sides(st)
        # print(len(st), sides)
        ans += len(st) * sides
    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
