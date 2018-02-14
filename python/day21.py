def main():

    puzzleInput = open("python/day21.txt", "r").read()

    # Part 1
    # assert(rotatePattern("123/456/789") == "369/258/147")
    # assert(flipPattern("123/456/789") == "321/654/987")
#     assert(part1("""../.# => ##./#../...
# .#./..#/### => #..#/..../..../#..#""") == "#..#/..../..../#..#")
    print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    print(part2(puzzleInput))

def part1(puzzleInput):

    # starting parttern
    pattern = ".#./..#/###"
    # startPattern = "123/456/789"
    # pattern = "1234/5678/90ab/cdef"
    # startPattern = "123456/78901a/cdefgh/ijklmn/opqrst/uvwyxz"

    rules = puzzleInput.split("\n")
    ruleBook = {}

    for rule in rules:
        parts = rule.split(" => ")
        ruleBook[parts[0]] = parts[1]
    
    for i in range(0,5):
        pattern = sqaureToNewSwquare(pattern, ruleBook)
        # print("newPattern", pattern)
        # print()
    # count hash
    count = 0
    for i in pattern:
        if i == "#":
            count += 1

    return count

def part2(puzzleInput):

    # starting parttern
    pattern = ".#./..#/###"
    # startPattern = "123/456/789"
    # pattern = "1234/5678/90ab/cdef"
    # startPattern = "123456/78901a/cdefgh/ijklmn/opqrst/uvwyxz"

    rules = puzzleInput.split("\n")
    ruleBook = {}

    for rule in rules:
        parts = rule.split(" => ")
        ruleBook[parts[0]] = parts[1]
    
    for i in range(0,18):
        print(i)
        pattern = sqaureToNewSwquare(pattern, ruleBook)
        # print("newPattern", pattern)
        # print()
    # count hash
    count = 0
    for i in pattern:
        if i == "#":
            count += 1
            
    return count

def sqaureToNewSwquare(startPattern, ruleBook):
    
    pattern = startPattern.split("/")
    length = len(pattern[0])

    if (length % 2 == 0):
        newSquareSize = 2
        jumpBy = 2
    elif (length % 3 == 0):
        newSquareSize = 3
        jumpBy = 3

    # print(pattern)
    subSqaures = []
    # Find start squares
    for i in range(0,length,jumpBy):
        for k in range(0,length,jumpBy):
            # Build sub squares
            newSubSquare = []
            for x in range(0,newSquareSize):
                for y in range(0,newSquareSize):
                    # print(i+x,k+y)
                    newSubSquare.append(pattern[i+x][k+y])
                newSubSquare.append("/")
            subSqaures.append(newSubSquare)

    # print("mixed", subSqaures)
    # Create sub patterns from each array
    for i in range(0,len(subSqaures)):
        subSqaures[i] = "".join(subSqaures[i])[:-1]
    # print("rejoin", subSqaures)

    # get new patterns 
    for i in range(0,len(subSqaures)):
        subSqaures[i] = getNewPattern(ruleBook, subSqaures[i])
    # print("new returned pattern", subSqaures)
        
    # split retunr patterns
    for i in range(0,len(subSqaures)):
        subSqaures[i] = subSqaures[i].split("/")
    
    # print("cleaned", subSqaures)

    # Recombine back into square
    length += 1
    newPattern = ""
    rowSpread = int(length/newSquareSize)
    for i in range(0,rowSpread**2,rowSpread):
        emptyArray = [""]*(newSquareSize + 1)

        for j in range(i,i+rowSpread):
            for k in range(0,newSquareSize+1):
                emptyArray[k] += subSqaures[j][k]
        for i in emptyArray:
            newPattern += i + "/"
    newPattern = newPattern[:-1]

    return newPattern

def getNewPattern(ruleBook, currentPattern):
    # Get all possiblities of current pattern
    pVersions = getPatternVersions(currentPattern)
    # print(pVersions)
    # print(ruleBook)
    
    newPattern = ""
    for i in pVersions:
        match =(ruleBook.get(i,0))
        if match != 0:
            newPattern = match

    return newPattern 


def getPatternVersions(pattern):

    versions = []
    for i in range(0,4):
        rotated = rotatePattern(pattern)
        fliped = flipPattern(rotated)
        versions.append(rotated)
        versions.append(fliped)
        pattern = rotated
    return versions


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
            
if __name__ == "__main__":
    main()