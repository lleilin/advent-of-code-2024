SIDE_LENGTH = 71

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def parse_input(path, bytes):
    grid = [["." for _ in range(SIDE_LENGTH)] for _ in range(SIDE_LENGTH)]
    with open(path) as file:
        for _ in range(bytes):
            row = file.readline()
            if not row:
                return grid
            x, y = row.strip().split(",")
            x, y = int(x), int(y)
            grid[y][x] = "#"
    return grid


def part1(path, bytes):
    grid = parse_input(path, bytes)

    queue = [(0, 0)]
    ans = 0
    while True:
        ans += 1
        new_queue = []
        for i, j in queue:
            for di, dj in DIRECTIONS:
                ni, nj = i + di, j + dj
                if 0 <= ni < SIDE_LENGTH and 0 <= nj < SIDE_LENGTH and grid[nj][ni] == ".":
                    grid[nj][ni] = "#"
                    if ni == SIDE_LENGTH - 1 and nj == SIDE_LENGTH - 1:
                        return ans
                    new_queue.append((ni, nj))
        queue = new_queue
        if not queue:
            return -1


def part2(path):
    l = 0
    r = SIDE_LENGTH * SIDE_LENGTH

    while l < r:
        m = (l + r + 1) // 2
        val = part1(path, m)
        print(l, r, m, val)
        if val == -1:
            r = m
        else:
            l = m + 1

    with open(path) as file:
        rows = file.readlines()
        return l, rows[l-1].strip()


if __name__ == "__main__":
    # print(part1("input.txt", 1024))
    print(part2("input.txt"))
