
def main():

    puzzleInput = list(open("python/day01.txt", "r").read())

    # Part 1

    assert(part1(list("1122")) == 3)
    assert(part1(list("1111")) == 4)
    assert(part1(list("1234")) == 0)
    assert(part1(list("91212129")) == 9)

    res1 = part1(puzzleInput)
    print(res1)

    # Part 2

    assert(part2(list("1212")) == 6)
    assert(part2(list("1221")) == 0)
    assert(part2(list("123425")) == 4)
    assert(part2(list("123123")) == 12)
    assert(part2(list("12131415")) == 4)

    res2 = part2(puzzleInput)
    print(res2)


def part2(puzzleInput):

    total = 0
    inputSize = len(puzzleInput)
    for i in range(0, inputSize):
        otherHalf = int((inputSize/2 + i) % inputSize)
        if (puzzleInput[i] == puzzleInput[otherHalf]):
            total += int(puzzleInput[i])

    return total

def part1(puzzleInput):

    total = 0
    current = puzzleInput[-1]
    for num in puzzleInput:
        if (num == current):
            total += int(num)
        current = num

    return total

if __name__ == "__main__":
    main()