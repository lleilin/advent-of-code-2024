def parse_input(path):
    with open(path) as file:
        row = file.readline()
        bank = row.strip().split(",")
        bank = [w.strip() for w in bank]
        targets = []

        file.readline()
        for row in file:
            targets.append(row.strip())

        return bank, targets


def part1(path):
    word_bank, targets = parse_input(path)

    def helper(word, word_bank):
        n = len(word)
        dp = [True] + [False] * n

        for i in range(1, n + 1):
            for w in word_bank:
                start = i - len(w)
                if start >= 0 and dp[start] and word[start:i] == w:
                    dp[i] = True
                    break
        return dp[-1]

    ans = 0
    for word in targets:
        if helper(word, word_bank):
            ans += 1

    return ans


def part2(path):
    word_bank, targets = parse_input(path)

    def helper(word, word_bank):
        n = len(word)
        dp = [1] + [0] * n

        for i in range(1, n + 1):
            for w in word_bank:
                start = i - len(w)
                if start >= 0 and dp[start] and word[start:i] == w:
                    dp[i] += dp[start]
        return dp[-1]

    ans = 0
    for word in targets:
        tmp = helper(word, word_bank)
        # print(word, tmp)
        ans += tmp

    return ans


if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
