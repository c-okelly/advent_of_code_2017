def main():

    puzzleInput = open("python/day19.txt", "r").read()

    # Part 1
    assert(part1("""     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ """) == "ABCDEF")
    print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    # print(part2(puzzleInput))

def part1(puzzleInput):
    rows = puzzleInput.split("\n")

    # Build grid
    grid = {}
    mazeStart = (0, 0)
    rowNumber = 0
    for row in rows:
        # print(row, rowNumber)
        for i in range(0,len(row)):
            # print(row[i])
            if row[i] == "|":
                grid[(i, rowNumber)] = row[i]
            elif row[i] == "-":
                grid[(i, rowNumber)] = row[i]
            elif row[i] == "+":
                grid[(i, rowNumber)] = row[i]
            elif row[i].isalpha():
                grid[(i, rowNumber)] = row[i]
            if row[i] != " " and rowNumber == 0:
                mazeStart = (i, rowNumber)

        rowNumber -= 1

    # print(grid)
    # print(mazeStart)
    # Navigate maze
    letters = ""
    directions = [[0,-1],[0,1],[-1,0],[1,0]]
    currDirection = directions[0]
    currentPos = mazeStart
    visited = set()
    count = 1
    while True:
        # Check if direction exists
        posFound = False
        if grid.get(currentPos,"").isalpha():
            letters += grid[currentPos]

        if grid[currentPos] == "+":
            newDirections = directions[:]
            newDirections.remove(currDirection)
            for i in newDirections:
                newPos = (currentPos[0]+i[0],currentPos[1]+i[1])
                if grid.get(newPos, 0) != 0 and newPos not in visited:
                    currDirection = i
                    # print("newPos", newPos)
                    temp = newPos
                    posFound = True
            # print(newPos, "set")
            currentPos = temp
            count += 1
        else:
            currentPos = (currentPos[0]+currDirection[0],currentPos[1]+currDirection[1])
            if grid.get(currentPos, 0) != 0:
                count += 1
                posFound = True

        if posFound == False:
            break
        else:
            visited.add(currentPos)
            # print(grid[currentPos], currentPos)
    print("steps", count)
    return letters 

def part2(puzzleInput):

    return 0

if __name__ == "__main__":
    main()