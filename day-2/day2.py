def part1(path):
    input = open(path, "r")
    ans = 0
    for row in input:
        tmp = [int(i) for i in row.split()]
        if part1helper(tmp):
            ans += 1
    
    return ans

def part2(path):
    input = open(path, "r")
    ans = 0
    for row in input:
        tmp = [int(i) for i in row.split()]
        if part2helper(tmp):
            ans += 1
            continue
    
    return ans

def part1helper(row):
    # print(row)
    if row[1]==row[0]:
        return False

    if row[1] > row[0]:
        st = {1,2,3}
    else:
        st = {-1,-2,-3}

    for i in range(1,len(row)):
        if row[i]-row[i-1] not in st:
            return False
    return True

def part2helper(row):
    for idx in range(len(row)):
        tmp = row.copy()
        tmp.pop(idx)
        if part1helper(tmp):
            return True

    return False

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))