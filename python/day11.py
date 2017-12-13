def main():

    puzzleInput = open("python/day11.txt", "r").read()

    # Part 1
    assert(part1("ne,ne,ne") == 3)
    # assert(part1("ne,ne,ne") == 3)
    print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    # print(part2(puzzleInput))

def part1(puzzleInput):

    moves = puzzleInput.split(",")

    currPos = [0,0,0]
    for move in moves:
        if move == "n":
            currPos[1] = currPos[1] + 1
        # elif move == "ne":
        #     currPos[1] = currPos[1] + 1
        #     currPos[0] = currPos[0] + 1
        # elif move == "nw":
        #     currPos[1] = currPos[1] + 1
        #     currPos[0] = currPos[0] - 1

        # elif move == "s":
        #     currPos[1] = currPos[1] - 1
        # elif move == "se":
        #     currPos[1] = currPos[1] - 1
        #     currPos[0] = currPos[0] + 1
        # elif move == "sw":
        #     currPos[1] = currPos[1] - 1
        #     currPos[0] = currPos[0] - 1

    print(currPos)

    return 3

def part2(puzzleInput):

    return 0

if __name__ == "__main__":
    main()