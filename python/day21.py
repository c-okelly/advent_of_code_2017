def main():

    puzzleInput = open("python/day21.txt", "r").read()

    # Part 1
    assert(rotatePattern("123/456/789") == "369/258/147")
    assert(flipPattern("123/456/789") == "321/654/987")
#     assert(part1("""../.# => ##./#../...
# .#./..#/### => #..#/..../..../#..#""") == 0)
    # print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    # print(part2(puzzleInput))

def part1(puzzleInput):

    # starting parttern
    pattern = "123/456/789"

    rules = puzzleInput.split("\n")
    ruleBook = {}

    for rule in rules:
        parts = rule.split(" => ")
        ruleBook[parts[0]] = parts[1]
    
    # Get all possiblities of current pattern

    rotatePattern(pattern)


    return 0

def rotatePattern(pattern):

    rows = pattern.split("/")
    newPattern = []
    for i in range(0,len(rows)):
        newPattern.append([])
    for i in range(0,len(rows)):
        row = list(rows[i])
        for k in range(0,len(row)):
            newPattern[-k-1].append(row[k])
    result = ""
    for i in newPattern:
        result += "".join(i) + '/'

    return result[:-1]

def flipPattern(pattern):

    result = ""
    for i in pattern.split("/"):
        result += ''.join(i[::-1]) + "/"
    
    return result[:-1]
            
def part2(puzzleInput):

    return 0

if __name__ == "__main__":
    main()