import numpy as np

def part1(path):
    with open(path) as file:
        lines = file.readlines()
        ans = 0
        for n in range(0, len(lines), 4):
            (ax, ay) = (int(x) for x in lines[n][12:].split(", Y+"))
            (bx, by) = (int(x) for x in lines[n+1][12:].split(", Y+"))
            (px, py) = (int(x) for x in lines[n+2][9:].split(", Y="))
            
            A = np.array([[ax, bx], [ay, by]])
            B = np.array([px, py])
        
            solution = np.linalg.solve(A, B)
            
            if np.all(np.abs(solution - np.round(solution)) < 1e-5) and np.all(solution >= 0):
                solution = np.round(solution).astype(int)
                tokens = 3 * solution[0] + solution[1]
                ans += tokens
        
        return ans
    
def part2(path):
    with open(path) as file:
        lines = file.readlines()
        ans = 0
        for n in range(0, len(lines), 4):
            (ax, ay) = (int(x) for x in lines[n][12:].split(", Y+"))
            (bx, by) = (int(x) for x in lines[n+1][12:].split(", Y+"))
            (px, py) = (int(x) for x in lines[n+2][9:].split(", Y="))
            
            px += 10000000000000
            py += 10000000000000

            A = np.array([[ax, bx], [ay, by]])
            B = np.array([px, py])
        
            solution = np.linalg.solve(A, B)
            
            if np.all(np.abs(solution - np.round(solution)) < 1e-4) and np.all(solution >= 0):
                solution = np.round(solution).astype(int)
                tokens = 3 * solution[0] + solution[1]
                ans += tokens
        
        return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
