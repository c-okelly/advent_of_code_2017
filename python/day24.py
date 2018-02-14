def main():

    puzzleInput = open("python/day24.txt", "r").read()

    # Part 1
    # assert(part1("") == 0)
    # print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    print(part2(puzzleInput))

def part1(puzzleInput):

    # Parse input
    bridgeSections = []
    for i in puzzleInput.split("\n"):
        bridgeSections.append([int(i.split("/")[0]), int(i.split("/")[1])])

    currentBridges = []
    finishedBridges = []
    # Find start sections
    for i in bridgeSections:
        if i[0] == 0 or i[1] == 0 :
            if i[0] != 0:
                start = i[::-1]
            else:
                start = i
            partsLeft = bridgeSections[:] 
            partsLeft.remove(i)
            currentBridges.append({"currentStructure": [start], "partsLeft": partsLeft})
    
    # build as many new bridges as possible
    while (len(currentBridges) > 0):
        current = currentBridges.pop(0)
        endPoint = current.get("currentStructure")[-1][1]
        # print(endPoint)

        sectionFound = False
        for section in current.get("partsLeft"):
            if section[0] == endPoint or section[1] == endPoint:
                sectionFound = True
                if section[0] == endPoint:
                    newSection = section[:]
                else:
                    newSection = section[:][::-1]
                # print(section, newSection)

                # make new part
                newBridge = current.get("currentStructure")[:]
                newBridge.append(newSection)

                partsLeft = current.get("partsLeft")[:] 
                partsLeft.remove(section)
                # print(newBridge)
                # print(partsLeft)
                # print()
                currentBridges.append({"currentStructure": newBridge, "partsLeft": partsLeft})
        
        if sectionFound == False:
            # print("finished")
            finishedBridges.append(current)


    # find longest bridge
    len(finishedBridges)
    maxLength = 0
    for bridge in finishedBridges:
        bridgeSections = bridge.get("currentStructure")
        currenTotal = 0
        for sec in bridgeSections:
            for part in sec:
                currenTotal += part
                
        if currenTotal > maxLength:
            maxLength = currenTotal

    return maxLength

def part2(puzzleInput):

    # Parse input
    bridgeSections = []
    for i in puzzleInput.split("\n"):
        bridgeSections.append([int(i.split("/")[0]), int(i.split("/")[1])])

    currentBridges = []
    finishedBridges = []
    # Find start sections
    for i in bridgeSections:
        if i[0] == 0 or i[1] == 0 :
            if i[0] != 0:
                start = i[::-1]
            else:
                start = i
            partsLeft = bridgeSections[:] 
            partsLeft.remove(i)
            currentBridges.append({"currentStructure": [start], "partsLeft": partsLeft})


    # build as many new bridges as possible
    while (len(currentBridges) > 0):
        current = currentBridges.pop(0)
        endPoint = current.get("currentStructure")[-1][1]
        # print(endPoint)

        sectionFound = False
        for section in current.get("partsLeft"):
            if section[0] == endPoint or section[1] == endPoint:
                sectionFound = True
                if section[0] == endPoint:
                    newSection = section[:]
                else:
                    newSection = section[:][::-1]
                # print(section, newSection)

                # make new part
                newBridge = current.get("currentStructure")[:]
                newBridge.append(newSection)

                partsLeft = current.get("partsLeft")[:] 
                partsLeft.remove(section)
                currentBridges.append({"currentStructure": newBridge, "partsLeft": partsLeft})
        
        if sectionFound == False:
            finishedBridges.append(current)


    longestBridges = []
    longest = 0
    for i in finishedBridges:
        if len(i.get("currentStructure")) >= longest:
            longestBridges.append(i)
            longest = len(i.get("currentStructure"))
    
    finalLongest = []
    for i in longestBridges:
        if len(i.get("currentStructure")) == longest:
            finalLongest.append(i)
    
    maxLength = 0
    for bridge in finalLongest:
        bridgeSections = bridge.get("currentStructure")
        currenTotal = 0
        for sec in bridgeSections:
            for part in sec:
                currenTotal += part
                
        if currenTotal > maxLength:
            maxLength = currenTotal
        
    return maxLength

if __name__ == "__main__":
    main()