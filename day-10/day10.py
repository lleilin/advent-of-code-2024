from functools import cache


def part1(path):
    grid = []

    with open(path) as file:
        for row in file:
            grid.append([])
            for c in row.rstrip():
                if c.isdigit():
                    grid[-1].append(int(c))
                else:
                    grid[-1].append(-1)

    # for row in grid:
    #     print(row)

    m, n = len(grid), len(grid[0])
    # print(m,n)

    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def part1_helper(r, c):
        if grid[r][c] != 0:
            return 0
        curr = set([(r, c)])
        for height in range(1,10):
            new_curr = set()
            for i,j in curr:
                for di,dj in DIRECTIONS:
                    if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj] == height:
                        new_curr.add((i+di, j+dj))
            curr = new_curr
        return len(curr)

    ans = 0
    part1_helper(0,3)
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                continue
            ans += part1_helper(i, j)

    return ans

def part2(path):
    grid = []

    with open(path) as file:
        for row in file:
            grid.append([])
            for c in row.rstrip():
                if c.isdigit():
                    grid[-1].append(int(c))
                else:
                    grid[-1].append(-1)

    # for row in grid:
    #     print(row)

    m, n = len(grid), len(grid[0])
    # print(m,n)

    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def part1_helper(r, c):
        if grid[r][c] != 0:
            return 0
        curr = [(r, c)]
        for height in range(1,10):
            new_curr = []
            for i,j in curr:
                for di,dj in DIRECTIONS:
                    if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj] == height:
                        new_curr.append((i+di, j+dj))
            curr = new_curr
        return len(curr)

    ans = 0
    part1_helper(0,3)
    for i in range(m):
        for j in range(n):
            if grid[i][j] != 0:
                continue
            ans += part1_helper(i, j)

    return ans


if __name__ == "__main__":
    # print(part1("input.txt"))
    print(part2("input.txt"))
