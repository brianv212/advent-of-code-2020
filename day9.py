def get_int(line):
    if '\n' in line:
        l = line[:-1]
    return int(l)

def check_sum(line,ensemble):
    num = get_int(line)
    found = {}
    for item in ensemble:
        if item in found.keys():
            return True
        found[num-item] = item
    return False

def contiguous(ensemble):
    position = 0
    pos_a = 0
    current_sum = 0
    current_vals = []
    while True and pos_a < len(ensemble) - 1:
        if current_sum == 90433990:
            return min(current_vals) + max(current_vals)

        elif current_sum > 90433990:
            current_sum = 0
            current_vals = []
            pos_a += 1
            position = pos_a
        else:
            current_sum += ensemble[position]
            current_vals.append(ensemble[position])
        position += 1
    return None



def run_main():
    ensemble = []
    historical = []
    with open("input9.txt", "r") as fp:
        line = fp.readline()
        while line:
            if len(ensemble) == 25:
                check = check_sum(line, ensemble)
                if check is not True:
                    historical += ensemble
                    return contiguous(historical)
                historical.append(ensemble[-1])
                ensemble.pop(0)
            ensemble.append(get_int(line))
            line = fp.readline()

if __name__ == "__main__":
    print("Advent of Code: Day 9 - Encoding Error")
    answer = run_main()
    print("(Part 2) Sum of max and min:", answer)