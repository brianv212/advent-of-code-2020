def gather_info():
    instructions = []
    with open("input8.txt", "r") as fp:
        line = fp.readline()
        while line:
            if '\n' in line:
                instructions.append(line[:-1])
            else:
                instructions.append(line)
            line = fp.readline()
        fp.close()
    return instructions

def handle_instruction(instruction):
    split = instruction.split(' ')
    if split[0] == "acc":
        val = int(split[1][1:])
        if split[1][0] == "-":
            val *= -1
        return val, 1
    elif split[0] == "jmp":
        val = int(split[1][1:])
        if split[1][0] == "-":
            val *= -1
        return 0, val
    return 0, 1

def run_part_one():
    accumulator = 0
    seen = []
    instructions = gather_info()
    position = 0
    while True:
        if position < 0 or position > len(instructions) - 1:
            break
        if position in seen:
            return accumulator
        else:
            info = handle_instruction(instructions[position])
            seen.append(position)
            accumulator += info[0]
            position += info[1]
    return accumulator
        




if __name__ == "__main__":
    print("Advent of Code: Day 8 - Handheld Halting")
    answer = run_part_one()
    print("Value of the accumulator:", answer)
    # answer = run_part_two()
    # print(answer)
