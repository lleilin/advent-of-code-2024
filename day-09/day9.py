def part1(path):
    arr = []
    with open(path) as file:
        line = file.readline()
        arr = list(line)

    new_arr = []
    id_number = 0
    for i, val in enumerate(arr):
        if i % 2 == 0:
            for _ in range(int(val)):
                new_arr.append(id_number)
            id_number += 1
        else:
            for _ in range(int(val)):
                new_arr.append(None)

    l, r = 0, len(new_arr) - 1

    while l < r:
        while new_arr[l] != None:
            l += 1
        while not new_arr[r]:
            r -= 1
        if l >= r:
            break
        new_arr[l] = new_arr[r]
        new_arr[r] = None
        l += 1
        r -= 1
    ans = 0
    for idx, val in enumerate(new_arr):
        if val == None:
            break
        ans += idx * val
    return ans


def part2(path):
    with open(path) as file:
        line = file.readline()
        arr = list(line)

    fs = []
    id_number = 0
    index = 0
    for i, val in enumerate(arr):
        if i % 2 == 0:
            fs.append([index, int(val), id_number])
            id_number += 1
        else:
            fs.append([index, int(val), None])
        index += int(val)

    curr_id_number = fs[-1][2]

    # print(fs)

    while True:
        if curr_id_number == 0:
            break
        p
        back_idx = len(fs)-1
        while fs[back_idx][2] != curr_id_number:
            back_idx -= 1
        _, length, id_number = fs[back_idx]
        fs[back_idx][2] = None

        front_idx = 0
        while fs[front_idx][2]!=None or fs[front_idx][1] < length:
            front_idx += 1

        # print(fs[front_idx][1] < length)

        fs.insert(front_idx, [fs[front_idx][0], length, id_number])
        # print(fs[front_idx][0], length, id_number)
        fs[front_idx+1][0] += length
        fs[front_idx+1][1] -= length

        curr_id_number -= 1
    
    # print(fs)
    ans = 0
    for start, length, val in fs:
        if val == None:
            continue
        for i in range(start, start+length):
            # print(i,val)
            ans += (i*val)
            

    return ans

if __name__ == "__main__":
    # print(part1("input.txt"))
    print(part2("input.txt"))
