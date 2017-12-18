def main():

    puzzleInput = open("python/day17.txt", "r").read()

    # Part 1
    assert(part1("3") == 638)
    print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    print(part2(puzzleInput))

def part1(puzzleInput):

    buffer = [0]

    step = int(puzzleInput)
    bufferPos = 0 + step

    for i in range(1, 2018):
        bufferPos = (bufferPos + step) % len(buffer)
        # print(bufferPos, bufferPos+step, len(buffer))
        if (bufferPos+ 1 == len(buffer)):
            buffer.append(i)
        else:
            buffer.insert(bufferPos+1, i)
        bufferPos += 1
        # print(buffer)

    return buffer[(bufferPos+1)%len(buffer)] 

def part2(puzzleInput):

    buffer = [0, 1]

    step = int(puzzleInput)
    bufferPos = 0 + step
    bufferLength = 1

    for i in range(1, 50000000):
        bufferPos = (bufferPos + step) % bufferLength
        if bufferPos == 0:
            buffer[1] = i
        elif bufferPos == (bufferLength - 1):
            buffer[1] = buffer[0]
            buffer[0] = i
        bufferPos += 1
        bufferLength += 1

    # print(buffer)
    return buffer[1]

if __name__ == "__main__":
    main()
