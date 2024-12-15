from functools import cache


def parse_input(path):
    grid = []
    commands = []

    is_grid = True
    with open(path) as file:
        for line in file:
            if is_grid:
                if not line.strip():
                    is_grid = False
                else:
                    grid.append(list(line.strip()))
            else:
                commands.extend(line.strip())

    return grid, commands


dir_map = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


def find_robot(grid):
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == "@":
                return i, j
    assert False


def move(grid, direction):
    start_i, start_j = find_robot(grid)
    di, dj = dir_map[direction]

    i, j = start_i + di, start_j + dj
    if grid[i][j] == "#":
        return

    if grid[i][j] == ".":
        grid[start_i][start_j], grid[i][j] = grid[i][j], grid[start_i][start_j]

    if grid[i][j] == "O":
        next_i, next_j = i, j
        while grid[next_i][next_j] != ".":
            if grid[next_i][next_j] == "#":
                return
            next_i += di
            next_j += dj
        assert grid[next_i][next_j] == "."
        grid[next_i][next_j] = "O"
        assert grid[next_i][next_j] == "O"
        grid[i][j] = "@"
        grid[start_i][start_j] = "."


def help_print(grid):
    print("PRINTING GRID:")
    for row in grid:
        print(row)


def part1(path):
    grid, commands = parse_input(path)
    for command in commands:
        move(grid, command)

    # help_print(grid)
    ans = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == "O":
                ans += 100 * i
                ans += j
    return ans


def parse_input2(path):
    grid = []
    commands = []

    is_grid = True
    with open(path) as file:
        for line in file:
            if is_grid:
                if not line.strip():
                    is_grid = False
                else:
                    grid.append([])
                    for i in line.strip():
                        if i == "O":
                            grid[-1].append("[")
                            grid[-1].append("]")
                        elif i == "@":
                            grid[-1].append("@")
                            grid[-1].append(".")
                        else:
                            grid[-1].append(i)
                            grid[-1].append(i)
            else:
                commands.extend(line.strip())

    return grid, commands


def move2(grid, direction):
    start_i, start_j = find_robot(grid)
    di, dj = dir_map[direction]
    st = set()

    @cache
    def check(i, j, direction):
        assert direction in "^v"
        di, _ = dir_map[direction]
        if grid[i][j] == "@":
            st.add((i,j))
            return check(i + di, j, direction)
        if grid[i][j] == "#":
            return False
        if grid[i][j] == ".":
            return True

        if grid[i][j] == "[":
            st.add((i,j))
            st.add((i, j+1))
            return check(i + di, j, direction) and check(
                i + di, j + 1, direction
            )
        if grid[i][j] == "]":
            st.add((i,j))
            st.add((i,j-1))
            return check(i + di, j, direction) and check(
                i + di, j - 1, direction
            )

        assert False

    if direction == "<":
        next_j = start_j - 1
        if grid[start_i][start_j - 1] == "#":
            return
        while grid[start_i][next_j] in "[]":
            next_j -= 1
        
        if grid[start_i][next_j] == "#":
            return

        for tmp in range(next_j, start_j):
            grid[start_i][tmp] = grid[start_i][tmp + 1]
        grid[start_i][start_j] = "."
        return

    if direction == ">":
        next_j = start_j + 1
        if grid[start_i][start_j + 1] == "#":
            return
        while grid[start_i][next_j] in "[]":
            next_j += 1
        
        if grid[start_i][next_j] == "#":
            return

        for tmp in range(next_j, start_j, -1):
            grid[start_i][tmp] = grid[start_i][tmp - 1]
        grid[start_i][start_j] = "."
        return

    st.clear()
    if check(start_i, start_j, direction):
        # print(st)
        if direction == "^":
            for i,j in sorted(st):
                grid[i-1][j] = grid[i][j]
                grid[i][j] = '.'
        if direction == "v":
            for i,j in sorted(st, reverse=True):
                grid[i+1][j] = grid[i][j]
                grid[i][j] = '.'


def part2(path):
    grid, commands = parse_input2(path)
    # help_print(grid)

    # move2(grid, "v")

    # help_print(grid)

    for command in commands:
        # print(command)
        # help_print(grid)
        move2(grid, command)

    # help_print(grid)
    ans = 0
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == "[":
                ans += 100 * i
                ans += j
    return ans
    


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
