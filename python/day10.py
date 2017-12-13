def main():

    puzzleInput = open("python/day10.txt", "r").read()

    # Part 1
    # assert(part1("3,4,1,5") == 12)
    print(part1(puzzleInput))
    
    # # Part 2
    assert(part2("") == "a2582a3a0e66e6e86e3812dcb672a272")
    assert(part2("") == "33efeb34ea91902bb2f59c9920caa6cd")
    assert(part2("") == "3efbe78a8d82f29979031a4aa0b16a9d")
    assert(part2("") == "63960835bcdc130f0b66d7ff4f6a5a8e")
    # print(part2(puzzleInput))

def part1(puzzleInput):

    currentArray = list(range(0,256))
    instructions = [int(x.strip()) for x in puzzleInput.split(",")]

    currentPos = 0
    skipSize = 0
    while (len(instructions) > 0):
        # Identify sub arrays to be swapped
        currentLength = instructions.pop(0)
        firstSection = list(range(currentPos, int(currentLength/2)+currentPos))
        if (currentLength % 2 == 1):
            secSection = list(range(int(currentLength/2 + 1)+currentPos, currentLength+currentPos))
        else:
            secSection = list(range(int(currentLength/2)+currentPos, currentLength+currentPos))

        # print(firstSection, secSection)

        # Perform swap

        currentPos += (currentLength + skipSize) % len(currentArray)
        skipSize += 1

        newArray = currentArray[:]

        count = 0
        for i in firstSection[::-1]:
            newArray[i % len(currentArray)] = currentArray[secSection[count] % len(currentArray)]
            count += 1
        count = 0
        for i in secSection[::-1]:
            newArray[i % len(currentArray)] = currentArray[firstSection[count] % len(currentArray)]
            count += 1

        currentArray = newArray[:]
        # print(newArray)

    return currentArray[0] * currentArray[1]

def part2(puzzleInput):

    return 0

if __name__ == "__main__":
    main()