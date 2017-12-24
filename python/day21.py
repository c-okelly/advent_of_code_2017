def main():

    puzzleInput = open("python/day21.txt", "r").read()

    # Part 1
    assert(part1("""../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#""") == 0)
    # print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    # print(part2(puzzleInput))

def part1(puzzleInput):

    # starting parttern
    pattern = ".#./..#/###"

    rules = puzzleInput.split("\n")
    ruleBook = {}

    for rule in rules:
        parts = rule.split(" => ")
        ruleBook[parts[0]] = parts[1]
    
    # Rotate until ma


    return 0

def part2(puzzleInput):

    return 0

if __name__ == "__main__":
    main()