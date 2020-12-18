categories = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"] # Global var used by all functions

def handle_birthyear(data): # Index 0
    try:
        if 1920 <= int(data) <= 2010:
            return True
        else:
            return False
    except:
        return False

def handle_issue_year(data): # Index 1
    try:
        if 2010 <= int(data) <= 2020:
            return True
        else:
            return False
    except:
        return False

def handle_exp_year(data): # Index 2
    try:
        if 2020 <= int(data) <= 2030:
            return True
        else:
            return False
    except:
        return False

def handle_height(data): # Index 3
    bounds = []
    if "cm" in data or "in" in data:
        classifier = data[-2:]
        if classifier == "cm":
            bounds.append(150)
            bounds.append(193)
        elif classifier == "in":
            bounds.append(59)
            bounds.append(76)
        else:
            return False
        
    if len(bounds) == 2:
        try:
            if bounds[0] <= int(data[:-2]) <= bounds[1]:
                return True
            else:
                return False
        except:
            return False
    return False


def handle_hair_color(data): # Index 4
    if data[0] == '#' and len(data) == 7:
        for i in range(1,len(data)):
            asc = ord(data[i])
            if asc <= 47 or (58 <= asc <= 96) or (103 <= asc):
                return False
        return True
    return False


def handle_eye_color(data): # Index 5
    colors = ["amb","blu","brn","gry","grn","hzl","oth"]
    if data in colors:
        return True
    return False

def handle_passport_id(data): # Index 6
    if len(data) == 9 and data.isdigit():
        return True
    return False

def handle_country_id(data): # Index 7
    return True

def handle_information(pos,data): #returns bool: True = valid, False = invalid.
    functions = [handle_birthyear,handle_issue_year, handle_exp_year,handle_height,
       handle_hair_color,handle_eye_color,handle_passport_id,handle_country_id]
    return functions[pos](data[1])


def process_data(data):
    validation = [None] * len(categories)
    debugging = [None] * len(categories)
    for item in data:
        line = item.split(' ')
        for d in line:
            info = d.split(':')
            if '\n' in info[1]:
                info[1] = info[1][:-1]

            # Process information: info[0] = category, info[1] = description
            if info[0] in categories:
                pos = categories.index(info[0])
                valid = handle_information(pos,info)
                validation[pos] = valid
                debugging[pos] = info[1]

            else: # Invalid category name
                return 0
    for i in range(len(validation) - 1):
        if validation[i] == False or validation[i] == None:
            return 0
    return 1


def debug():
    functions = [handle_birthyear,handle_issue_year, handle_exp_year,handle_height,
                 handle_hair_color,handle_eye_color,handle_passport_id,handle_country_id]
    print(functions[0]("2000"))
    print(functions[1]("2010"))
    print(functions[2]("2025"))
    print(functions[3]("60in"))
    print(functions[4]("#ag1092"))
    print(functions[5]("brn"))
    print(functions[6]("021938232"))
    print(functions[7]("??"))


if __name__ == "__main__":
    print("Advent of Code: Day 4 - Passport Processing")

    debug()
    
    valid_passports = 0

    with open("input4.txt", "r") as fp:
        line = fp.readline()
        data = []
        while line:
            if line == "\n":
                valid_passports += process_data(data)
                data = []
            else:
                data.append(line)
            line = fp.readline()

    print("Valid Passports:", valid_passports)
