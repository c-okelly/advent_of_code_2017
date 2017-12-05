import math
import numpy

def main():

    puzzleInput = open("python/day03.txt", "r").read()


    # Part 1
    # assert(part1("1") == 1)
    # assert(part1("12") == 3)
    # assert(part1("23") == 2)
    # assert(part1("1024") == 31)
    # print(part1(puzzleInput))
    
    # Part 2
    print(part2(puzzleInput))
    # print(getNewSquareCorrds((1,-1),3))

def part1(puzzleInput):
    sqaure = int(puzzleInput)
    # Sum = (2n + 1)^2 => 4n^2 + 4n + 1
    a, b = 4, 4
    c = 1 - int(puzzleInput)
    d = (b**2) - (4*a*c)

    sol1 = (-b-math.sqrt(d))/(2*a)
    sol2 = (-b+math.sqrt(d))/(2*a)
    
    # print(sol1, sol2)
    layer = int(sol2) + 1
    # print(layer)

    layerSide = int((squareSize(layer)-squareSize(layer-1)) / 4)
    minDis = layerSide
    for i in range(squareSize(layer)-layer,squareSize(layer-1),-layerSide):
        distance = abs(i - int(puzzleInput))
        if (distance < minDis):
            minDis = distance
            # print(distance)
    # print(minDis,layer, "min")
    return minDis + layer

# def getNextPos(current,gird)

def part2(puzzleInput):

    grid = {}
    nextPos = makeGrid(10)
    # print(nextPos)
    newVal = 0

    for i in nextPos:
        if (i == (0,0)):
            grid[(0,0)] = 1
        else:
            newVal = getNewValue(grid, i)
            print(newVal)
            grid[(i)] = newVal
        if (newVal > int(puzzleInput)):
            break

    return newVal

def makeGrid(size):

    grid = [(0, 0)]
    layer = 1
    while layer < size:
        #R
        side = 1 + (layer * 2)
        grid.append((grid[-1][0]+1, grid[-1][1]))
        #U
        for i in range(0,side-2):
            grid.append((grid[-1][0],grid[-1][1]+1))
        # L
        for i in range(0,side-1):
            grid.append((grid[-1][0]-1, grid[-1][1]))
        # D
        for i in range(0,side-1):
            grid.append((grid[-1][0], grid[-1][1]-1))
        # R
        for i in range(0,side-1):
            grid.append((grid[-1][0]+1, grid[-1][1]))
        layer += 1
        # print(grid)
    return grid





def getNewValue(dataStruct, position):

    cords = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    total = 0
    for i in cords:
        x = position[0] + i[0]
        y = position[1] + i[1]
        total += dataStruct.get((x,y),0)
    return total

def setValue(matrix,pos1,pos2,value):

    matrix[0][0] = value

def squareSize(layerNo):

    layerSize = 4*layerNo**2 + 4*layerNo + 1

    return layerSize  

if __name__ == "__main__":
    main()