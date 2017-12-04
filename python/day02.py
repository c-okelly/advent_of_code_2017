
def main():

    puzzleInput = open("python/day02.txt", "r").read()

    # Part 1
    assert(part1("5 1 9 5") == 8)
    assert(part1("7 5 3") == 4)
    assert(part1("2 4 6 8") == 6)
    print(part1(puzzleInput))
    
    # Part 2
    assert(part2("5 9 2 8") == 4)
    assert(part2("9 4 7 3") == 3)
    assert(part2("3 8 6 5") == 2)
    print(part2(puzzleInput))

def part1(puzzleInput):

    rows = puzzleInput.split("\n")

    total = 0
    for row in rows:
        splitRow = row.split()
        min = int(splitRow[0])
        max = int(splitRow[0])

        for i in splitRow:
            if int(i) < min:
                min = int(i)
            if int(i) > max:
                max = int(i)
        diff = abs(max - min)
        total += diff

    return total

def part2(puzzleInput):

    rows = puzzleInput.split("\n")

    total = 0
    for row in rows:
        splitRow = row.split()
        for i in range(0,len(splitRow)):
            first = int(splitRow[i])
            for v in range(0,len(splitRow)):
                sec = int(splitRow[v])
                if (first == sec):
                    break
                elif first % sec == 0:
                    total += first/sec
                elif sec % first == 0:
                    total += sec/first
    return total

if __name__ == "__main__":
    main()