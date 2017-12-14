def main():

    puzzleInput = open("python/day10.txt", "r").read()

    # Part 1
    # assert(part1("3,4,1,5") == 12)
    # print(part1(puzzleInput))
    
    # # Part 2
    assert(splitArray([1,2,3,4,5,6],3) == [[1,2,3],[4,5,6]])
    assert(getXor([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]) == 64)
    assert(part2("") == "a2582a3a0e66e6e86e3812dcb672a272")
    assert(part2("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd")
    assert(part2("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d")
    assert(part2("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e")
    print(part2(puzzleInput))

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

    return currentArray[0] * currentArray[1]

def part2(puzzleInput):

    # Convert input to asci code
    # Add suffix
    instructions = []
    for i in puzzleInput:
        instructions.append(ord(i))
    instructions.extend([17, 31, 73, 47, 23])

    # print(instructions)

    # Run 64 rounds
    currentArray = list(range(0,256))
    currentPos = 0
    skipSize = 0

    for i in range(0,64):
        cunrentInstructions = instructions[:]
        while (len(cunrentInstructions) > 0):
            # Identify sub arrays to be swapped
            currentLength = cunrentInstructions.pop(0)
            firstSection = list(range(currentPos, int(currentLength/2)+currentPos))
            if (currentLength % 2 == 1):
                secSection = list(range(int(currentLength/2 + 1)+currentPos, currentLength+currentPos))
            else:
                secSection = list(range(int(currentLength/2)+currentPos, currentLength+currentPos))

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
    
    # Split array into chunks
    currentArray = splitArray(currentArray,16)

    # xor each chunck
    denseHash = []
    for i in currentArray:
        denseHash.append(getXor(i))

    # convert each chunck to hex
    finalString = ""
    for i in denseHash:
        hexValue = hex(i)[2:]
        if len(hexValue) == 1:
            hexValue = "0" + hexValue
        finalString += hexValue

    return finalString

def getXor(array):
    curValue = 0
    for value in array:
        curValue = curValue ^ value 
    return curValue

def splitArray(currentArray, splitSize):
    
    newArray = []
    for i in range(0, len(currentArray), splitSize):
        newArray.append(currentArray[i:i+splitSize])
    return newArray

if __name__ == "__main__":
    main()