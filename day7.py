def process_data(info, search):
    split_info = info.split("bags contain")
    container = None
    for item in search:
        if item in split_info[1]:
            container = split_info[0][:-1]
            break
    return container



def run_part_one():
    contains = ["shiny gold"]
    while True:
        info_gain = 0
        with open("input7.txt", "r") as fp:
            line = fp.readline()
            while line:
                info = process_data(line, contains)
                if info is not None and info not in contains:
                    contains.append(info)
                    info_gain += 1
                line = fp.readline()
        if info_gain == 0:
            break
    return len(contains) - 1

def gather_info(info, search):

def run_part_two():
    searching = ["shiny gold"]
    while True:
        info_gain = 0
        with open("input7.txt", "r") as fp:
            line = fp.readline()
            while line:
                info = process_data(line, contains)
                line = fp.readline()
        if info_gain == 0:
            break

if __name__ == "__main__":
    print("Advent of Code: Day 7 - Handy Haversacks")
    answer = run_part_one()
    print("Bags with Shiny Gold:", answer)
    # answer = run_part_two()
    # print(answer)
