def main():

    puzzleInput = open("python/day05.txt", "r").read()

    # Part 1
    assert(part1("""0
    3
    0
    1
    -3""") == 5)
    print(part1(puzzleInput))
    
    # Part 2
    assert(part2("""0
    3
    0
    1
    -3""") == 10)
    print(part2(puzzleInput))

def part1(puzzleInput):

    instructions = list(map(int, puzzleInput.split("\n")))

    position = 0
    jumps = 0
    while position < len(instructions):
        newPos = position + instructions[position]
        instructions[position] = instructions[position] + 1
        position = newPos
        jumps += 1

    return jumps

def part2(puzzleInput):

    instructions = list(map(int, puzzleInput.split("\n")))

    position = 0
    jumps = 0
    while position < len(instructions):
        newPos = position + instructions[position]
        if (instructions[position]) >= 3:
            instructions[position] = instructions[position] - 1
        else:
            instructions[position] = instructions[position] + 1
        position = newPos
        jumps += 1

    return jumps

if __name__ == "__main__":
    main()