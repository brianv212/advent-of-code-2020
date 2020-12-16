# DAY 1

year = 2020
# Sum of two numbers = 2020
def sum_of_two(nums):
    seen = {}
    for x in nums:
        if year-x in seen.keys():
            print(x*seen[year-x])
        else:
            seen[x] = x

# Sum of three numbers = 2020
def sum_of_three(nums):
    seen = {}
    for x in nums:
        for y in nums:
            for z in nums:
                if x+y+z == year:
                    print(x*y*z)
                    return
                    
if __name__ == "__main__":
    print("Advent of Code: Day 1 - Report Repair")
    nums = []

    with open("input1.txt", "r") as fp:
        line = fp.readline()
        while line:
            nums.append(int(line))
            line = fp.readline()

    sum_of_two(nums)
    sum_of_three(nums)
