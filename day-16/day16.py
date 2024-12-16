from heapq import heappop, heappush, heapify

# EAST, SOUTH, WEST, NORTH
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def parse_input(path):
    grid = []
    with open(path) as file:
        for row in file:
            grid.append(list(row.strip()))

    return grid


def help_print(grid):
    print("PRINTING GRID:")
    for row in grid:
        print(row)


def find_value(grid, value):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == value:
                return i, j
    assert False


def part1(path):
    grid = parse_input(path)
    start_i, start_j = find_value(grid, "S")

    # score, i,j, direction
    queue = [(0, start_i, start_j, 0)]
    visited = set()

    while True:
        score, i, j, d = heappop(queue)
        # print(score, i, j, d)
        if grid[i][j] == "E":
            return score

        # GO FORWARD
        di, dj = DIRECTIONS[d]
        if grid[i + di][j + dj] != "#" and (i + di, j + dj, d) not in visited:
            heappush(queue, (score + 1, i + di, j + dj, d))
            visited.add((i + di, j + dj, d))

        # TURN LEFT
        l = (d + 3) % 4
        if (i, j, l) not in visited:
            heappush(queue, (score + 1000, i, j, l))
            visited.add((i, j, l))

        # TURN RIGHT
        r = (d + 1) % 4
        if (i, j, r) not in visited:
            heappush(queue, (score + 1000, i, j, r))
            visited.add((i, j, r))


def part2(path):
    grid = parse_input(path)
    m, n = len(grid), len(grid[0])
    # print(start_end)
    start_i, start_j = find_value(grid, "S")
    end_i, end_j = find_value(grid, "E")

    queue = [(0, start_i, start_j, 0)]
    start_end = [[[float("inf") for _ in range(4)] for _ in range(n)] for _ in range(m)]
    start_end[start_i][start_j][0] = 0

    while queue:
        score, i, j, d = heappop(queue)

        # GO FORWARD
        di, dj = DIRECTIONS[d]
        if grid[i + di][j + dj] != "#" and start_end[i + di][j + dj][d] == float("inf"):
            heappush(queue, (score + 1, i + di, j + dj, d))
            start_end[i + di][j + dj][d] = score + 1

        # TURN LEFT
        l = (d + 3) % 4
        if start_end[i][j][l] == float("inf"):
            heappush(queue, (score + 1000, i, j, l))
            start_end[i][j][l] = score + 1000

        # TURN RIGHT
        r = (d + 1) % 4
        if start_end[i][j][r] == float("inf"):
            heappush(queue, (score + 1000, i, j, r))
            start_end[i][j][r] = score + 1000

    queue = [(0, end_i, end_j, d) for d in range(4)]
    heapify(queue)
    end_start = [[[float("inf") for _ in range(4)] for _ in range(n)] for _ in range(m)]
    for d in range(4):
        end_start[end_i][end_j][d] = 0

    while queue:
        score, i, j, d = heappop(queue)
        # GO FORWARD
        di, dj = DIRECTIONS[d]
        if grid[i + di][j + dj] != "#" and end_start[i + di][j + dj][d] == float("inf"):
            heappush(queue, (score + 1, i + di, j + dj, d))
            end_start[i + di][j + dj][d] = score + 1

        # TURN LEFT
        l = (d + 3) % 4
        if end_start[i][j][l] == float("inf"):
            heappush(queue, (score + 1000, i, j, l))
            end_start[i][j][l] = score + 1000

        # TURN RIGHT
        r = (d + 1) % 4
        if end_start[i][j][r] == float("inf"):
            heappush(queue, (score + 1000, i, j, r))
            end_start[i][j][r] = score + 1000

    # help_print(start_end)
    # help_print(end_start)

    best_score = float("inf")
    ans = 1

    for i in range(m):
        for j in range(n):
            tmp = float('inf')
            for d in range(4):
                total = start_end[i][j][d] + end_start[i][j][(d+2)%4]
                tmp = min(tmp, total)
            
            if tmp == best_score:
                ans += 1

            if tmp < best_score:
                best_score = tmp
                ans = 1
                
    # print(ans, best_score)
    return ans


if __name__ == "__main__":
    # print(part1("input.txt"))
    print(part2("input.txt"))
