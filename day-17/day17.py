def parse_input(path):
    with open(path) as file:
        data = file.readlines()

        a = int(data[0].split()[-1])
        b = int(data[1].split()[-1])
        c = int(data[2].split()[-1])

        instructions = data[4].split()[-1].split(",")
        instructions = [int(i) for i in instructions]
        return a, b, c, instructions


def run(a, b, c, instructions):
    reg_a, reg_b, reg_c = a, b, c
    instructions = instructions
    i = 0
    ans = []
    while i < len(instructions):
        opcode = instructions[i]
        literal_operand = instructions[i + 1]
        i += 2

        combo_operand = literal_operand
        match combo_operand:
            case 4:
                combo_operand = reg_a
            case 5:
                combo_operand = reg_b
            case 6:
                combo_operand = reg_c

        match opcode:
            case 0:
                reg_a = reg_a >> combo_operand
            case 1:
                reg_b = reg_b ^ literal_operand
            case 2:
                reg_b = combo_operand % 8
            case 3:
                i = literal_operand if reg_a != 0 else i
            case 4:
                reg_b = reg_b ^ reg_c
            case 5:
                ans.append(combo_operand % 8)
            case 6:
                reg_b = reg_a >> combo_operand
            case 7:
                reg_c = reg_a >> combo_operand
    return ans


def part1(path):
    a, b, c, instructions = parse_input(path)

    print(run(a, b, c, instructions))
    print(run(117440, b, c, instructions))


def helper(a, b, c, instructions):
    reg_a, reg_b, reg_c = a, b, c
    i = 0
    ans = []
    while i < len(instructions):
        opcode = instructions[i]
        literal_operand = instructions[i + 1]
        i += 2

        combo_operand = literal_operand
        match combo_operand:
            case 4:
                combo_operand = reg_a
            case 5:
                combo_operand = reg_b
            case 6:
                combo_operand = reg_c

        match opcode:
            case 0:
                reg_a = reg_a >> combo_operand
            case 1:
                reg_b = reg_b ^ literal_operand
            case 2:
                reg_b = combo_operand % 8
            case 3:
                i = literal_operand if reg_a != 0 else i
            case 4:
                reg_b = reg_b ^ reg_c
            case 5:
                ans.append(combo_operand % 8)
                if len(ans) > len(instructions):
                    return False
                if ans[len(ans) - 1] != instructions[len(ans) - 1]:
                    return False
            case 6:
                reg_b = reg_a >> combo_operand
            case 7:
                reg_c = reg_a >> combo_operand
    if len(ans) != len(instructions):
        return False
    return True


def find_a(a, b, c, instructions, prg_pos):
    if abs(prg_pos) > len(instructions):
        return a
    for i in range(8):
        first_digit_out = run(a * 8 + i, b, c, instructions)[0]
        if first_digit_out == instructions[prg_pos]:
            e = find_a(a * 8 + i, b, c, instructions, prg_pos - 1)
            if e:
                return e


def part2(path):
    _, b, c, instructions = parse_input(path)
    return find_a(0, b, c, instructions, -1)


if __name__ == "__main__":
    # print(part1("input.txt"))
    print(part2("input.txt"))

7, 1, 5, 2, 4, 0, 7, 6, 1
