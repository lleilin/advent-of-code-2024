from termcolor import colored

WIDTH = 101
HEIGHT = 103


def part1(path):
    quadrants = [0, 0, 0, 0]
    with open(path) as file:
        for row in file:
            tmp = row.strip()
            p, v = tmp.split()
            _, p = p.split("=")
            _, v = v.split("=")

            x, y = p.split(",")
            dx, dy = v.split(",")
            x, y = int(x), int(y)
            dx, dy = int(dx), int(dy)

            # print(x, y, dx, dy)
            x = (x + (100 * dx)) % WIDTH
            y = (y + (100 * dy)) % HEIGHT

            # print(x,y)
            if x < WIDTH // 2 and y < HEIGHT // 2:
                quadrants[0] += 1
            if x < WIDTH // 2 and y > HEIGHT // 2:
                quadrants[1] += 1
            if x > WIDTH // 2 and y > HEIGHT // 2:
                quadrants[2] += 1
            if x > WIDTH // 2 and y < HEIGHT // 2:
                quadrants[3] += 1

    ans = 1
    for i in quadrants:
        ans *= i

    return ans


class Robot:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy

        self.x %= WIDTH
        self.y %= HEIGHT


class Simulator:
    def __init__(self, path):
        self.grid = [[[] for _ in range(WIDTH)] for _ in range(HEIGHT)]
        with open(path) as file:
            for row in file:
                tmp = row.strip()
                p, v = tmp.split()
                _, p = p.split("=")
                _, v = v.split("=")

                x, y = p.split(",")
                dx, dy = v.split(",")

                x, y = int(x), int(y)
                dx, dy = int(dx), int(dy)
                self.grid[y][x].append(Robot(x, y, dx, dy))

    def move_all(self):
        new_grid = [[[] for _ in range(WIDTH)] for _ in range(HEIGHT)]

        for i in range(HEIGHT):
            for j in range(WIDTH):
                for robot in self.grid[i][j]:
                    robot.move()
                    # print(robot.x, robot.y)
                    new_grid[robot.y][robot.x].append(robot)

        self.grid = new_grid

    def print(self):
        color_map = {
        'a': 'red',
        'b': 'green',
        'c': 'yellow',
        'd': 'blue',
        'e': 'magenta',
        'f': 'cyan',
        'g': 'white',
        # Add more mappings as needed
        }
        
        for row in self.grid:
            tmp = [chr(len(i) + ord('a')) for i in row]
            colored_row = [colored(char, color_map.get(char, 'white')) for char in tmp]
            print(''.join(colored_row))
    
    def check(self):
        for row in self.grid:
            for i in row:
                if len(i) > 1:
                    return False
        
        return True


def part2(path):
    s = Simulator(path)
    for i in range(8300):
        print("GENERATION", i)
        # s.print()
        if s.check():
            print(i)
            s.print()
            # return
        s.move_all()


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
