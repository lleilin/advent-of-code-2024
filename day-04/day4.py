def part1(path):
    with open(path) as file:
        grid = [row.rstrip() for row in file]

    m,n = len(grid), len(grid[0])
    word = ""
    ans = 0
    def help():
        if word == "XMAS":
            nonlocal ans
            ans += 1

    for i in range(m):
        for j in range(n):
            if 0<=i-3 and 0<=j-3:
                word = grid[i][j]+grid[i-1][j-1]+grid[i-2][j-2]+grid[i-3][j-3]
                help()
            if 0<=i-3:
                word = grid[i][j]+grid[i-1][j]+grid[i-2][j]+grid[i-3][j]
                help()
            if 0<=i-3 and j+3<n:
                word = grid[i][j]+grid[i-1][j+1]+grid[i-2][j+2]+grid[i-3][j+3]
                help()
            if j+3<n:
                word = grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i][j+3]
                help()
            if i+3<m and j+3<n:
                word = grid[i][j]+grid[i+1][j+1]+grid[i+2][j+2]+grid[i+3][j+3]
                help()
            if i+3<m:
                word = grid[i][j]+grid[i+1][j]+grid[i+2][j]+grid[i+3][j]
                help()
            if i+3<m and 0<=j-3:
                word = grid[i][j]+grid[i+1][j-1]+grid[i+2][j-2]+grid[i+3][j-3]
                help()
            if 0<=j-3:
                word = grid[i][j]+grid[i][j-1]+grid[i][j-2]+grid[i][j-3]
                help()
    return ans

def part2(path):
    with open(path) as file:
        grid = [row.rstrip() for row in file]
    
    m, n = len(grid), len(grid[0])
    ans = 0

    for i in range(1,m-1):
        for j in range(1,n-1):
            if grid[i][j] != 'A':
                continue
                
            if grid[i-1][j-1]=='M' and grid[i-1][j+1]=='M' and grid[i+1][j+1]=='S' and grid[i+1][j-1]=='S':
                ans += 1
            if grid[i-1][j-1]=='S' and grid[i-1][j+1]=='M' and grid[i+1][j+1]=='M' and grid[i+1][j-1]=='S':
                ans += 1
            if grid[i-1][j-1]=='S' and grid[i-1][j+1]=='S' and grid[i+1][j+1]=='M' and grid[i+1][j-1]=='M':
                ans += 1
            if grid[i-1][j-1]=='M' and grid[i-1][j+1]=='S' and grid[i+1][j+1]=='S' and grid[i+1][j-1]=='M':
                ans += 1
    return ans

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))