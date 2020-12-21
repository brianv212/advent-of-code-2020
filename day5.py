import math

def front_back(info):
    bounds =  [0,127]
    for i in range(len(info)):
        if info[i] == "F": # Lower Half
            constant = math.floor((bounds[1] - bounds[0])/2)
            bounds[1] = constant + bounds[0]
        elif info[i] == "B": # Upper Half
            constant = math.ceil((bounds[1] - bounds[0])/2)
            bounds[0] = constant + bounds[0]

        if i == len(info) - 1:
            return bounds[0] if info[i] == "F" else bounds[1]

def left_right(info):
    bounds = [0,7]
    for i in range(len(info)):
        if i == (len(info) - 1):
            return bounds[0] if info[i] == "L" else bounds[1]
        else:
            if info[i] == "L": # Lower Half
                constant = math.floor((bounds[1] - bounds[0])/2)
                bounds[1] = constant + bounds[0]
            elif info[i] == "R": # Upper Half
                constant = math.ceil((bounds[1] - bounds[0])/2)
                bounds[0] = constant + bounds[0] 



def get_seat_number(line):
    if line[-1] == '\n':
        line = line[:-1]
    fb = front_back(line[0:7])
    lr = left_right(line[7:])
    return fb * 8 + lr




def run_main():
    seats = [i for i in range(823)]
    highest_seat_number = 0
    debug = None
    with open("input5.txt", "r") as fp:
        line = fp.readline()
        while line:
            seat = get_seat_number(line)
            if seat > highest_seat_number:
                highest_seat_number = seat
                debug = line
            if seat in seats:
                seats.remove(seat)
            line = fp.readline()
    get_seat_number(debug)
    return highest_seat_number, seats

if __name__ == "__main__":
    print("Advent of Code: Day 5 - Passport Processing")
    answer = run_main()
    print("Highest seat number:", answer[0])
    print("My seat:", answer[1][-1])