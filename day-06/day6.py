def part1(path):
    grid = []
    with open(path) as file:
        for row in file:
            grid.append(list(row.rstrip()))

    m, n = len(grid), len(grid[0])

    visited = set()

    def find_guard() -> tuple[int, int]:
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "^":
                    grid[i][j] = "."
                    return (i, j)

    i, j = find_guard()
    curr_dir = 0

    # for row in grid:
    #     print(row)

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while 0 <= i < m and 0 <= j < n:
        visited.add((i, j))
        di, dj = directions[curr_dir]
        if 0 <= i + di < m and 0 <= j + dj < n and grid[i + di][j + dj] != ".":
            curr_dir = (curr_dir + 1) % 4
            continue
        i, j = i + di, j + dj

    return len(visited)


def part2(path):
    grid = []
    with open(path) as file:
        for row in file:
            grid.append(list(row.rstrip()))

    m, n = len(grid), len(grid[0])

    def find_guard():
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "^":
                    grid[i][j] = "."
                    return i, j

    start_i, start_j = find_guard()

    curr_dir = 0

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def traverse(i, j):
        visited = set()
        curr_dir = 0

        while 0 <= i < m and 0 <= j < n:
            if (i, j, curr_dir) in visited:
                return False
            visited.add((i, j, curr_dir))
            di, dj = directions[curr_dir]
            if (
                0 <= i + di < m
                and 0 <= j + dj < n
                and grid[i + di][j + dj] != "."
            ):
                curr_dir = (curr_dir + 1) % 4
                continue
            i, j = i + di, j + dj

        return True

    ans = 0
    for i in range(n):
        for j in range(m):
            if i==start_i and j == start_j:
                continue
            if grid[i][j] == ".":
                grid[i][j] = "#"
                if not traverse(start_i, start_j):
                    # print(i,j)
                    ans += 1
                grid[i][j] = "."
    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
