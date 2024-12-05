from collections import defaultdict


def part1(path):
    ans = 0
    mp = defaultdict(set)
    with open(path) as file:
        for row in file:
            tmp = row.rstrip()
            if not tmp:
                break
            X, Y = tmp.split("|")
            # X needs to be before Y
            # if X is after Y bad
            mp[Y].add(X)

        def helper(arr):
            for idx, val in enumerate(arr):
                for j in arr[idx + 1 :]:
                    if j in mp[val]:
                        return False
            return True

        for row in file:
            tmp = row.rstrip()
            arr = tmp.split(",")
            if helper(arr):
                mid = arr[len(arr) // 2]
                ans += int(mid)
    return ans


def part2(path):
    ans = 0
    mp = defaultdict(set)
    with open(path) as file:
        for row in file:
            tmp = row.rstrip()
            if not tmp:
                break
            X, Y = tmp.split("|")
            # X needs to be before Y
            # if X is after Y bad
            mp[Y].add(X)
            # X < Y

        def helper(arr):
            for idx, val in enumerate(arr):
                for j in arr[idx + 1 :]:
                    if j in mp[val]:
                        return False
            return True

        def part2_helper(arr):
            from graphlib import TopologicalSorter

            ts = TopologicalSorter()
            for val in arr:
                ts.add(val, *mp[val])
            order = {val: idx for idx, val in enumerate(ts.static_order())}
            arr.sort(key=lambda x: order[x])

            return arr[len(arr)//2]

        for row in file:
            tmp = row.rstrip()
            arr = tmp.split(",")
            if helper(arr):
                continue
            ans += int(part2_helper(arr))

    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
