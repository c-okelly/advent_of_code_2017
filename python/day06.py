def main():

    puzzleInput = open("python/day06.txt", "r").read()

    # Part 1
    assert(part1("0 2   7   0") == 5)
    print(part1(puzzleInput))
    
    # Part 2
    assert(part2("0 2   7   0") == 4)
    print(part2(puzzleInput))

def part1(puzzleInput):

    banks = list(map(int, puzzleInput.split()))
    # print(banks)
    count = 0

    state = set()
    while True:
        count += 1
        # Find max
        maxPos = 0
        largest = banks[0]
        for i in range(0,len(banks)):
            if banks[i] > largest:
                maxPos = i
                largest = banks[i]

        # print(maxPos)
        
        spread = banks[maxPos]
        banks[maxPos] = 0
        currentPos = maxPos + 1
        while spread > 0:
            currentPos = currentPos % len(banks)
            banks[currentPos] = banks[currentPos] + 1
            currentPos += 1
            spread -= 1


        # print(banks)
        currentState = tuple(banks)
        if (currentState not in state):
            state.add(currentState)
        else:
            break

    return count

def part2(puzzleInput):

    banks = list(map(int, puzzleInput.split()))
    # print(banks)
    count = 0
    loopSize = 0

    state = {}
    while True:
        count += 1
        # Find max
        maxPos = 0
        largest = banks[0]
        for i in range(0,len(banks)):
            if banks[i] > largest:
                maxPos = i
                largest = banks[i]

        # print(maxPos)
        
        spread = banks[maxPos]
        banks[maxPos] = 0
        currentPos = maxPos + 1
        while spread > 0:
            currentPos = currentPos % len(banks)
            banks[currentPos] = banks[currentPos] + 1
            currentPos += 1
            spread -= 1


        # print(banks)
        currentState = tuple(banks)
        if (currentState not in state):
            state[currentState] = count
        else:
            lastSeen = state[currentState]
            loopSize = count - lastSeen
            break

    return loopSize

if __name__ == "__main__":
    main()