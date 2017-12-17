from collections import Counter
from day10 import part2 as day10

def main():

    puzzleInput = open("python/day14.txt", "r").read()

    # Part 1
    # assert(part1("flqrgnkx") == 8108)
    # print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    assert(part2("flqrgnkx") == 1242)
    # print(part2(puzzleInput))

def part1(puzzleInput):

    puzzleInput = puzzleInput.strip()
    binaryString = ""
    for i in range(0,128):
        row = str(day10(puzzleInput+"-"+str(i)))
        binaryRow = bin(int(row, 16))[2:]
        binaryRow = "0" * (128 - len(binaryRow)) + binaryRow
        binaryString += binaryRow

    c = Counter(list(binaryString))

    return c["1"]

def part2(puzzleInput):
    
    # Build grid
    grid = {}
    neighbours = {}

    puzzleInput = puzzleInput.strip()
    binaryString = ""
    for i in range(0,128):
        row = str(day10(puzzleInput+"-"+str(i)))
        binaryRow = bin(int(row, 16))[2:]
        binaryRow = "0" * (128 - len(binaryRow)) + binaryRow
        # print(binaryRow)
        for z in range(0,128):
            cord = (z,i)
            grid[cord] = binaryRow[z]
            neighbours[cord] = []
            # print(binaryRow[z])
            # if binaryRow[z] == "1":
            #     # Check if has neighbours
            #     if grid.get((z-1,i),0) == "1":
            #         neighbours[cord].append((z-1,i))
            #     if grid.get((z,i-1),0) == "1":
            #         neighbours[cord].append((z,i-1))

    # flesh out grid
    for key in grid.keys():
        # print(key, grid[key])
        if (grid.get(key) == "1"):
            if grid.get((key[0]+1,key[1]),"0") == "1":
                neighbours[key].append((key[0]+1,key[1]))
            if grid.get((key[0]-1,key[1]),"0") == "1":
                neighbours[key].append((key[0]-1,key[1]))
            if grid.get((key[0],key[1]+1),"0") == "1":
                neighbours[key].append((key[0],key[1]+1))
            if grid.get((key[0],key[1]-1),"0") == "1":
                neighbours[key].append((key[0],key[1]-1))


    print(neighbours[(4, 4)])
    for key in neighbours.keys():
        exploredPipes = set()
        unexplored = [key]

        while len(unexplored) > 0:
            currentPipe = unexplored.pop(0)
            newPipes = neighbours.get(currentPipe, [])
            for i in newPipes:
                if i not in exploredPipes:
                    exploredPipes.add(i)
                    unexplored.append(i)
                    if i not in neighbours[key]:
                        neighbours[key].append(i)

    # print(neighbours[(2,4)])
    groups = set()
    for i in neighbours.keys():
        groups.add(tuple(sorted(neighbours[i])))
    print(len(groups))
    return 0 #len(groups)

if __name__ == "__main__":
    main()