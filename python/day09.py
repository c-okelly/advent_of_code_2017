def main():

    puzzleInput = open("python/day09.txt", "r").read()

    # Part 1
    assert(part1("{}") == 1)
    assert(part1("{{{}}}") == 6)
    assert(part1("{{},{}}") == 5)
    assert(part1("{<{},{},{{}}>}") == 1)
    assert(part1("{{<a>},{<a>},{<a>},{<a>}}") == 9)
    assert(part1("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9)
    assert(part1("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3)
    print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    # print(part2(puzzleInput))

def part1(puzzleInput):

    totalScore = 0
    rows = puzzleInput.split("\n")

    brackets = 0
    garbage = 0
    for row in rows:
        # print(row)
        # Strip void characters
        allChars = list(row)
        legalChars = []
        inGarbage = False
        while(len(allChars) > 0):
            currentChar = allChars.pop(0)
            if currentChar == "!":
                allChars.pop(0)
            elif currentChar == "<":
                inGarbage = True 
            elif currentChar == ">":
                inGarbage = False
            else:
                if (inGarbage == False):
                    legalChars.append(currentChar)
                elif inGarbage == True:
                    garbage += 1
        # print(legalChars)

        for i in legalChars:
            # print(i)
            if i == "{":
                brackets += 1
            elif i == "}":
                brackets -= 1
                # print("LB = ", rightBracket)
                totalScore += brackets + 1

    print(garbage)
    return totalScore 

def part2(puzzleInput):

    return 0

if __name__ == "__main__":
    main()