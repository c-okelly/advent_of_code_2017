def main():

    puzzleInput = open("python/day15.txt", "r").read()

    # Part 1
    # assert(part1("") == 588)
    # print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 309)
    print(part2(puzzleInput))

def part1(puzzleInput):

    puzzleInput = puzzleInput.split("\n")
    a = int(puzzleInput[0].split(" ")[-1])
    b = int(puzzleInput[1].split(" ")[-1])
    matchCount = 0
    for i in range(0, 40_000_000):
        a = genA(a)
        b = genB(b)
        aBi = "0" * 16 + str(bin(a)[2:])
        bBi = "0" * 16 + str(bin(b)[2:])
        if str(aBi)[-16:] == str(bBi)[-16:]:
            matchCount += 1

    return matchCount

def part2(puzzleInput):

    puzzleInput = puzzleInput.split("\n")
    a = int(puzzleInput[0].split(" ")[-1])
    b = int(puzzleInput[1].split(" ")[-1])
    matchCount = 0

    for i in range(0, 5_000_000):
        while True:
            a = genA(a)
            if a % 4 == 0:
                break
        while True:
            b = genB(b)
            if b % 8 == 0:
                break
        aBi = "0" * 16 + str(bin(a)[2:])
        bBi = "0" * 16 + str(bin(b)[2:])
        if str(aBi)[-16:] == str(bBi)[-16:]:
            matchCount += 1
            # print(matchCount, i)

    return matchCount

def genA(num):
    factor = 16807
    num *= factor
    num %= 2147483647
    return num

def genB(num):
    factor = 48271
    num *= factor
    num %= 2147483647
    return num

if __name__ == "__main__":
    main()