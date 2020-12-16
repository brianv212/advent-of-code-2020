
def search_map(slope,iteration,m):
    search = slope*iteration
    m_len = len(m) - 1   
    if m[(search % m_len)] == '#':
        return 1
    return 0
    


if __name__ == "__main__":
    print("Advent of Code: Day 3 - Toboggan Trajectory")
    trees1 = 0
    trees3 = 0
    trees5 = 0
    trees7 = 0
    trees2 = 0
    
    count = 0

    with open("input3.txt", "r") as fp:
        line = fp.readline()
        while line:
            if count == 0:
                if line[0] == '#':
                    trees3 += 1
            
            elif count != 0:
                trees1 += search_map(1,count,line)
                trees3 += search_map(3,count,line)
                trees5 += search_map(5,count,line)
                trees7 += search_map(7,count,line)

                if count % 2 == 0:
                    trees2 += search_map(1,count // 2,line)
            count += 1
            line = fp.readline()

    print("Trees in the way:", trees1)
    print("Trees in the way:", trees3)
    print("Trees in the way:", trees5)
    print("Trees in the way:", trees7)
    print("Trees in the way:", trees2)
    print(trees1*trees3*trees5*trees7*trees2)
