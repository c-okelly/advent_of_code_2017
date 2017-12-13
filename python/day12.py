def main():

    puzzleInput = open("python/day01.txt", "r").read()

    # Part 1
    assert(part1("""0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""") == 0)
    # print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    # print(part2(puzzleInput))

def part1(puzzleInput):

    connections = {}
    rows = puzzleInput.split("\n")
    for row in rows:
        start = row.split("<->")[0].strip()
        pipes = [x.strip() for x in row.split("<->")[1].strip().split(",")]
        # print(start, pipes)
        connections[start] = pipes

    print(connections)
    # add secondary connections
    searched = []

    key = 0
    unexplored = []
    while True:
        newPipes = connections.get(0)

    return 0

def part2(puzzleInput):

    return 0

if __name__ == "__main__":
    main()