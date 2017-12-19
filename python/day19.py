def main():

    puzzleInput = open("python/day01.txt", "r").read()

    # Part 1
    assert(part1("""     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ """) == "ABCDEF")
    # print(part1(puzzleInput))
    
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
        print(row, rowNumber)
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
                print(row[i], i, rowNumber)
            if row[i] != " " and rowNumber == 0:
                mazeStart = (i, rowNumber)

        rowNumber += 1

    # print(grid)
    # print(mazeStart)
    # Navigate maze
    letters = ""
    directions = {"up":[0,-1],"down":[0,1],"right":[1,0],"left":[-1,0]}
    currDirection = directions["down"]
    currentPos = mazeStart
    while True:
        # Check if direction exists
        if grid[currentPos] == "+":
            for key in directions.keys():
                # if (currDirection == directions[key]):
                #     continue
                newPos = (currentPos[0]+currDirection[0],currentPos[1]+currDirection[1])
                if grid.get(newPos, 0) != 0:
                    currDirection = directions[key]
                    print(currDirection, grid[newPos])

            currentPos = (currentPos[0]+currDirection[0],currentPos[1]+currDirection[1])
            print("stoped")
        else:
            currentPos = (currentPos[0]+currDirection[0],currentPos[1]+currDirection[1])
            print(grid[currentPos], currentPos)

        # Change direction if does not exist
        # If 

    return "ABCDEF"

def part2(puzzleInput):

    return 0

if __name__ == "__main__":
    main()