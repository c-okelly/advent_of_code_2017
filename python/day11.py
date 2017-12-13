def main():

    puzzleInput = open("python/day11.txt", "r").read()

    # Part 1
    assert(part1("ne,ne,ne") == 3)
    print(part1(puzzleInput))
    
    # Part 2
    print(part2(puzzleInput))

def part1(puzzleInput):

    moves = puzzleInput.split(",")

    currPos = [0,0,0]
    furthest = 0
    for move in moves:
        if move == "n":
            currPos[0] = currPos[0] + 1
            currPos[2] = currPos[2] - 1
        elif move == "ne":
            currPos[0] = currPos[0] + 1
            currPos[1] = currPos[1] - 1
        elif move == "nw":
            currPos[1] = currPos[1] + 1
            currPos[2] = currPos[2] - 1

        elif move == "s":
            currPos[0] = currPos[0] - 1
            currPos[2] = currPos[2] + 1
        elif move == "se":
            currPos[1] = currPos[1] - 1
            currPos[2] = currPos[2] + 1
        elif move == "sw":
            currPos[0] = currPos[0] - 1
            currPos[1] = currPos[1] + 1

        distance = (abs(currPos[0]) + abs(currPos[1]) + abs(currPos[2])) // 2

    return distance

def part2(puzzleInput):

    moves = puzzleInput.split(",")

    currPos = [0,0,0]
    furthest = 0
    for move in moves:
        if move == "n":
            currPos[0] = currPos[0] + 1
            currPos[2] = currPos[2] - 1
        elif move == "ne":
            currPos[0] = currPos[0] + 1
            currPos[1] = currPos[1] - 1
        elif move == "nw":
            currPos[1] = currPos[1] + 1
            currPos[2] = currPos[2] - 1

        elif move == "s":
            currPos[0] = currPos[0] - 1
            currPos[2] = currPos[2] + 1
        elif move == "se":
            currPos[1] = currPos[1] - 1
            currPos[2] = currPos[2] + 1
        elif move == "sw":
            currPos[0] = currPos[0] - 1
            currPos[1] = currPos[1] + 1

        distance = (abs(currPos[0]) + abs(currPos[1]) + abs(currPos[2])) // 2
        if distance > furthest:
            furthest = distance

    return furthest 

if __name__ == "__main__":
    main()