
def get_information(line):
    current = ""
    space_count = 0

    return_data = [None] * 2
    for char in line:
        if char == ':':
            continue

        
        if char == ' ':
            if space_count == 0:
                bounds = current.split("-")
                return_data[space_count] = [int(bounds[0]), int(bounds[1])]
            else:
                return_data[space_count] = current
            
            space_count += 1
            current = ""
        else:
            current += char
    return return_data[0],return_data[1],current
    


def check_password(line):
    bounds, letter, password = get_information(line)

    count = 0
    for l in password:
        if l == letter:
            count += 1
    if count >= bounds[0] and count <= bounds[1]:
        return 1
    return 0


def check_letter_position(line):
    positions, letter, password = get_information(line)
    if len(password)+1 < positions[1]:
        return 0

    else:
        if (password[positions[0] - 1] == letter) ^ (password[positions[1] - 1] == letter):
            return 1
        return 0



if __name__ == "__main__":
    print("Advent of Code: Day 2 - Password Philosophy")
    valid_part1 = 0
    valid_part2 = 0

    with open("input2.txt", "r") as fp:
        line = fp.readline()
        while line:
            valid_part1 += check_password(line)
            valid_part2 += check_letter_position(line)
            line = fp.readline()

    print("Valid Passwords:", valid_part1)
    print("Valid Passwords with letter at position:", valid_part2)
