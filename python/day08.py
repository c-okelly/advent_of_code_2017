def main():

    puzzleInput = open("python/day08.txt", "r").read()

    # Part 1
    assert(part1("""b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""") == 1)
    print(part1(puzzleInput))
    
    # # Part 2
    # assert(part2("") == 0)
    # print(part2(puzzleInput))

def part1(puzzleInput):
    rows = puzzleInput.split("\n")

    currentItems = {}
    highestEver = 0
    for row in rows:
        splitRow = row.split()
        # Set values
        valueToChange = splitRow[0]
        addSub = splitRow[1]
        changeValue = int(splitRow[2])

        comparedValue = currentItems.get(splitRow[4], 0)
        comparision = splitRow[5]
        comparedInt = int(splitRow[6])

        if addSub == "dec":
            changeValue *= -1
        expresionTrue = None
        if (comparision == "<"):
            expresionTrue = comparedValue < comparedInt
        elif (comparision == "<="):
            expresionTrue = comparedValue <= comparedInt
        elif (comparision == ">"):
            expresionTrue = comparedValue > comparedInt
        elif (comparision == ">="):
            expresionTrue = comparedValue >= comparedInt
        elif (comparision == "=="):
            expresionTrue = comparedValue == comparedInt
        elif (comparision == "!="):
            expresionTrue = comparedValue != comparedInt

        if (expresionTrue == True):
            # print(valueToChange, changeValue)
            newValue = currentItems.get(valueToChange, 0) + changeValue
            if newValue > highestEver:
                highestEver = newValue
            currentItems[valueToChange] = newValue 

    # print(currentItems)
    print(highestEver)
    return max(currentItems.values())


def part2(puzzleInput):

    return 0

if __name__ == "__main__":
    main()