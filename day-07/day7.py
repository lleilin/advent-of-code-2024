def part1(path):
    ans = 0
    with open(path) as file:
        for row in file:
            total,_,nums = row.partition(':')
            total = int(total)
            nums = [int(i) for i in nums.split()]

            if part1_helper(total, nums):
                ans += total
    return ans

def part1_helper(total, arr):
        curr_set = set()
        curr_set.add(arr[0])

        for i in arr[1:]:
            new_set = set()
            for v in curr_set:
                new_set.add(v*i)
                new_set.add(v+i)
            curr_set = new_set
        
        return total in new_set
    

def part2(path):
    ans = 0
    with open(path) as file:
        for row in file:
            total,_,nums = row.partition(':')
            total = int(total)
            nums = [int(i) for i in nums.split()]

            if part2_helper(total, nums):
                ans += total
    return ans

def part2_helper(total, arr):
    curr_set = set()
    curr_set.add(arr[0])

    for i in arr[1:]:
        new_set = set()
        for v in curr_set:
            new_string = str(v)+str(i)
            new_set.add(int(new_string))
            new_set.add(v*i)
            new_set.add(v+i)
        curr_set = new_set
    
    return total in new_set

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
