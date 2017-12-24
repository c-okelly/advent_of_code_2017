from operator import add
def main():

    puzzleInput = open("python/day22.txt", "r").read()

    # Part 1
    assert(part1("""..#
#..
...""") == 5587)
    print(part1(puzzleInput))
    
    # Part 2
#     assert(part2("""..#
# #..
# ...""") == 26)
    print(part2(puzzleInput))

def part1(puzzleInput):
    # Build grid
    startPos = [0, 0]
    grid = {}
    rows = puzzleInput.split("\n")
    noRows = len(rows)
    noColumns = len(list(rows[0]))

    for i in rows:
        for item in list(i):
            grid[tuple(startPos)] = item
            startPos[0] += 1
        startPos[0] = 0
        startPos[1] += 1
            
    # Iterate
    directions = [[0,1],[-1,0],[0,-1],[1,0]]
    currentDirection = 2
    currPosition = [noRows//2,noColumns//2]

    count = 0
    for i in range(0,10000):
        currentNode = grid.get(tuple(currPosition),".")
        if currentNode == ".":
            currentDirection = (currentDirection - 1) % 4
            grid[tuple(currPosition)] = "#"
            count += 1
        elif currentNode == "#":
            currentDirection = (currentDirection + 1) % 4
            grid[tuple(currPosition)] = "."
        # Move position
        # print(currPosition, grid[tuple(currPosition)], directions[currentDirection])
        currPosition = [currPosition[0] + directions[currentDirection][0], currPosition[1] + directions[currentDirection][1]]
        # print(currPosition)

    # print(count)

    return count

def part2(puzzleInput):

    startPos = [0, 0]
    grid = {}
    rows = puzzleInput.split("\n")
    noRows = len(rows)
    noColumns = len(list(rows[0]))

    for i in rows:
        for item in list(i):
            if item == "#":
                grid[tuple(startPos)] = "i"
            elif item == ".":
                grid[tuple(startPos)] = "c" 
            startPos[0] += 1
        startPos[0] = 0
        startPos[1] += 1
            
    # Iterate
    directions = [[0,1],[-1,0],[0,-1],[1,0]]
    currentDirection = 2
    currPosition = [noRows//2,noColumns//2]

    count = 0
    for i in range(0,10000000):
        currentNode = grid.get(tuple(currPosition),"c")

        if currentNode == "c":
            currentDirection = (currentDirection - 1) % 4
            grid[tuple(currPosition)] = "w"

        elif currentNode == "i":
            currentDirection = (currentDirection + 1) % 4
            grid[tuple(currPosition)] = "f"

        elif currentNode == "w":
            grid[tuple(currPosition)] = "i"
            count += 1

        elif currentNode == "f":
            currentDirection = (currentDirection + 2) % 4
            grid[tuple(currPosition)] = "c"

        # Move position
        # print(currPosition, grid[tuple(currPosition)], directions[currentDirection])
        currPosition = [currPosition[0] + directions[currentDirection][0], currPosition[1] + directions[currentDirection][1]]
        # print(currPosition)

    print(count)

    return count

    return 0

if __name__ == "__main__":
    main()