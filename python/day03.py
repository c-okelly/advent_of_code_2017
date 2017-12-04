import math
import numpy

def main():

    puzzleInput = open("python/day03.txt", "r").read()

    # Layer size calc
    # print(getLayerSize(2))

    # Part 1
    # assert(part1("1") == 1)
    # assert(part1("12") == 3)
    # assert(part1("23") == 2)
    # assert(part1("1024") == 31)
    # print(part1(puzzleInput))
    
    # Part 2
    print(part2(puzzleInput))

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

def part2(puzzleInput):

    seed = 11
    matrix = numpy.zeros(11)

    print(matrix)

    return 0

def setValue(matrix,pos1,pos2,value):

    matrix[0][0] = value

def squareSize(layerNo):

    layerSize = 4*layerNo**2 + 4*layerNo + 1

    return layerSize  

if __name__ == "__main__":
    main()