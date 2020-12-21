from collections import defaultdict

def process_data(data):
    answers = defaultdict(int)
    for line in data:
        for character in line:
            if character == '\n':
                pass
            else:
                answers[character] += 1

    part2 = 0
    for val in answers.values():
        if val == len(data):
            part2 += 1
    return part2

def run_main():
    questions_answered = 0
    with open("input6.txt", "r") as fp:
        line = fp.readline()
        group_data = []
        while line:
            if line == '\n':
                questions_answered += process_data(group_data)
                group_data = []
            else:
                group_data.append(line)
            line = fp.readline()
    questions_answered += process_data(group_data)
    return questions_answered


if __name__ == "__main__":
    print("Advent of Code: Day 6 - Custom Customs")
    answer = run_main()
    print("Questions answered:", answer)