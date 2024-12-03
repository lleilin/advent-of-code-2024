def part1(path):
    file = open(path, 'r')
    string = file.read()

    N = len(string)
    ans = 0
    i = 0
    # for i in range(N-4):
    while i < N-1:
        i += 1
        if string[i:i+4] == "mul(":
            c = i+5
            while string[c].isdigit():
                c += 1
            a = int(string[i+4:c])
            if string[c] != ',':
                continue

            r = c + 1
            while string[r].isdigit():
                r += 1
            b = int(string[c+1:r])
            if string[r] != ')':
                continue
            # print(a,b)
            ans += (a*b)
            i = r
    return ans

def part2(path):
    file = open(path, 'r')
    string = file.read()

    N = len(string)
    ans = 0
    i = 0
    enable = True
    # for i in range(N-4):
    while i < N:
        i += 1
        if string[i:i+4] == "do()":
            enable = True
            i = i+4
        if string[i:i+7] == "don't()":
            enable = False
            i = i+7
        if not enable:
            continue
        if string[i:i+4] == "mul(":
            c = i+5
            while string[c].isdigit():
                c += 1
            a = int(string[i+4:c])
            if string[c] != ',':
                continue

            r = c + 1
            while string[r].isdigit():
                r += 1
            b = int(string[c+1:r])
            if string[r] != ')':
                continue
            # print(a,b)
            ans += (a*b)
            i = r
    return ans

if __name__ == "__main__":
    # print(part1("input.txt"))
    print(part2("input.txt"))