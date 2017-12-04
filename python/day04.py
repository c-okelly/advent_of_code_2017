def main():

    puzzleInput = open("python/day04.txt", "r").read()

    # Part 1
    assert(part1("aa bb cc dd ee") == 1)
    assert(part1("aa bb cc dd aa") == 0)
    assert(part1("aa bb cc dd aaa") == 1)
    print(part1(puzzleInput))
    
    # Part 2
    assert(part2("abcde fghij") == 1)
    assert(part2("abcde xyz ecdab") == 0)
    assert(part2("a ab abc abd abf abj") == 1)
    assert(part2("iiii oiii ooii oooi oooo") == 1)
    assert(part2("oiii ioii iioi iiio") == 0)
    print(part2(puzzleInput))

def part1(puzzleInput):

    totalValid = 0
    rows = puzzleInput.split("\n")
    for row in rows:
        phrases = set()
        duplicate = True
        words = row.split()
        for word in words:
            if word in phrases:
                duplicate = False
            phrases.add(word)
        if (duplicate == True):
            totalValid += 1

    return totalValid

def part2(puzzleInput):

    totalValid = 0
    rows = puzzleInput.split("\n")
    for row in rows:
        phrases = set()
        duplicate = True
        words = row.split()
        for word in words:
            word = ''.join(sorted(word))
            if word in phrases:
                duplicate = False
            phrases.add(word)
        if (duplicate == True):
            totalValid += 1

    return totalValid

if __name__ == "__main__":
    main()