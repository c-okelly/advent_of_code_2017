def main():

    puzzleInput = open("python/day13.txt", "r").read()

    # Part 1
    assert(part1("""0: 3
1: 2
4: 4
6: 4""") == 24)
    print(part1(puzzleInput))
    
    # Part 2
    assert(part2("""0: 3
1: 2
4: 4
6: 4""") == 10)
    print(part2(puzzleInput))

def part1(puzzleInput):

    rows = puzzleInput.split("\n")
    layers = {}
    lastLayer = 0
    for row in rows:
        row = [int(x.strip()) for x in row.split(':')]
        layers[row[0]] = row[1]
        if row[0] > lastLayer:
            lastLayer = row[0]

    # print(layers, lastLayer)

    severity = 0
    for i in range(0,lastLayer+1):
        layerDepth = layers.get(i,0)
        # check if clash
        if layerDepth != 0:
            run = i // (layerDepth - 1)
            relPosition = i % (layerDepth - 1)
            if (run % 2 == 1): # up
                absPosition = (layerDepth - 1) - relPosition
            else: # Down
                absPosition = relPosition

            # print(i, run, relPosition, absPosition)
            if (absPosition == 0):
                severity += (layerDepth * i)

    return severity

def part2(puzzleInput):

    rows = puzzleInput.split("\n")
    layers = {}
    lastLayer = 0
    for row in rows:
        row = [int(x.strip()) for x in row.split(':')]
        layers[row[0]] = row[1]
        if row[0] > lastLayer:
            lastLayer = row[0]

    delay = 1
    while True:
        severity = 0
        for i in range(0, lastLayer + 1):
            layerDepth = layers.get(i, 0)
            # check if clash
            if layerDepth != 0:
                run = (i + delay) // (layerDepth - 1)
                relPosition = (i + delay) % (layerDepth - 1)
                if (run % 2 == 1):  # up
                    absPosition = (layerDepth - 1) - relPosition
                else:  # Down
                    absPosition = relPosition
                if (absPosition == 0):
                    severity = 1
                    break
        if severity == 0:
            break
        else:
            delay += 1

    return delay 

if __name__ == "__main__":
    main()
