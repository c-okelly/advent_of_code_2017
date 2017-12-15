from collections import Counter
from day10 import part2 as day10

def main():

    puzzleInput = open("python/day14.txt", "r").read()

    # Part 1
    assert(part1("flqrgnkx") == 8108)
    print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    # print(part2(puzzleInput))

def part1(puzzleInput):

    puzzleInput = puzzleInput.strip()
    binaryString = ""
    for i in range(0,128):
        row = str(day10(puzzleInput+"-"+str(i)))
        binaryRow = bin(int(row, 16))[2:]
        binaryRow = "0" * (128 - len(binaryRow)) + binaryRow
        print(binaryRow)
        binaryString += binaryRow

    c = Counter(list(binaryString))

    return c["1"]

def part2(puzzleInput):
    
    # Build grid

    # Check if has neigbours

    # Claculate sets of neighbours


    return 0

if __name__ == "__main__":
    main()