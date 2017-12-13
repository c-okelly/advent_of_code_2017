from collections import defaultdict

def main():

    puzzleInput = open("python/day12.txt", "r").read()

    # Part 1
    assert(part1("""0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5""") == 6)
    print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    print(part2(puzzleInput))

def part1(puzzleInput):

    connections = defaultdict(list)
    rows = puzzleInput.split("\n")
    for row in rows:
        start = row.split("<->")[0].strip()
        pipes = [x.strip() for x in row.split("<->")[1].strip().split(",")]
        # print(start, pipes)
        connections[start] = pipes

    # print(connections)
    # add secondary connections
    searched = []

    key = "0"
    exploredPipes = set()
    unexplored = [key]

    while len(unexplored) > 0:
        # print("enxplored", unexplored)
        currentPipe = unexplored.pop(0)
        # print(currentPipe)
        newPipes = connections.get(currentPipe, [])
        # print("new", newPipes)
        for i in newPipes:
            # print("i is", i)
            if i not in exploredPipes:
                exploredPipes.add(i)
                unexplored.append(i)
                if i not in connections[key]:
                    connections[key].append(i)

        #         print(connections[key])
        # print()

    # print(connections[key])
    return len(connections[key])

def part2(puzzleInput):

    connections = defaultdict(list)
    rows = puzzleInput.split("\n")
    for row in rows:
        start = row.split("<->")[0].strip()
        pipes = [x.strip() for x in row.split("<->")[1].strip().split(",")]
        connections[start] = pipes

    for key in connections.keys():
        exploredPipes = set()
        unexplored = [key]

        while len(unexplored) > 0:
            currentPipe = unexplored.pop(0)
            newPipes = connections.get(currentPipe, [])
            for i in newPipes:
                if i not in exploredPipes:
                    exploredPipes.add(i)
                    unexplored.append(i)
                    if i not in connections[key]:
                        connections[key].append(i)

    groups = set()
    for i in connections.keys():
        curr = set(frozenset(x) for x in connections[i])
        groups.add(curr)
    print(groups)
    return 0

if __name__ == "__main__":
    main()