def main():

    puzzleInput = open("python/day13.txt", "r").read()

    # Part 1
    assert(part1("""0: 3
1: 2
4: 4
6: 4""") == 0)
    # print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    # print(part2(puzzleInput))

def part1(puzzleInput):

    rows = puzzleInput.split("\n")
    layers = {}
    lastLayer = 0
    for row in rows:
        row = [int(x.strip()) for x in row.split(':')]
        layers[row[0]] = row[1]
        if row[0] > lastLayer:
            lastLayer = row[0]

    print(layers, lastLayer)

    severity = 0
    for i in range(0,lastLayer+1):
        layerDepth = layers.get(i,0)
        # check if clash
        if layerDepth != 0:


    return 0

def part2(puzzleInput):

    return 0

if __name__ == "__main__":
    main()
