def main():

    puzzleInput = open("python/day20.txt", "r").read()

    # Part 1
#     assert(part1("""p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>
# p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>""") == 0)
    print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    print(part2(puzzleInput))

def part1(puzzleInput):

    data = puzzleInput.split("\n")
    # Build data structure
    vectors = {}
    for v in range(0, len(data)):
        vec = data[v]
        info = vec.split(">")
        currentPos = [int(x) for x in info[0].split("<")[1].split(",")]
        velocity = [int(x) for x in info[1].split("<")[1].split(",")]
        acceleration = [int(x) for x in info[2].split("<")[1].split(",")]
        vectors[v] = {"p":currentPos, "v":velocity, "a":acceleration, "steady":False}

    # loop till we have steady state
    unsteady = 1
    time = 0
    while time < 1000:
        time += 1
        unsteady = 0
        for key in vectors.keys():
            vector = vectors[key]
            # Check steay state
            if vector["steady"] == False:
                unsteady += 1

            # Get new position and velocity
            oldVeloctiy = vector["v"][:]
            oldPosition = vector['p'][:]
            for i in range(0,3):
                vector["v"][i] += vector["a"][i]
                vector["p"][i] += vector["v"][i]

            # Compare old and new velocity so see if all part are accelerating
            nowSteady = True
            for i in range(0,3):
                if (abs(vector["v"][0]) - abs(oldVeloctiy[0]) < 0):
                    nowSteady = False
            # Check if still getting closer to origin
            if (sum([abs(x) for x in vector['p']]) < sum([abs(x) for x in oldPosition])):
                nowSteady = False

            vector["steady"] = nowSteady

    shortest = sum([abs(x) for x in vectors[0]['p']])
    closest = 0
    for key in vectors.keys():
        distance = sum([abs(x) for x in vectors[key]['p']])
        if distance < shortest:
            shortest = distance
            closest = key

    # print(vectors[closest])
    return closest 

def part2(puzzleInput):

    data = puzzleInput.split("\n")
    # Build data structure
    vectors = {}
    for v in range(0, len(data)):
        vec = data[v]
        info = vec.split(">")
        currentPos = [int(x) for x in info[0].split("<")[1].split(",")]
        velocity = [int(x) for x in info[1].split("<")[1].split(",")]
        acceleration = [int(x) for x in info[2].split("<")[1].split(",")]
        vectors[v] = {"p":currentPos, "v":velocity, "a":acceleration, "steady":False}
    
    time = 0
    while time < 1000:
        time += 1
        unsteady = 0
        allPos= {}
        for key in vectors.keys():
            vector = vectors[key]

            for i in range(0,3):
                vector["v"][i] += vector["a"][i]
                vector["p"][i] += vector["v"][i]
            currentPos = tuple(vector['p'][:])

            if len(allPos.get(currentPos, [])) > 0:
                allPos[currentPos].append(key)
            else:
                allPos[currentPos] = [key]

        for i in allPos.keys():
            if len(allPos[i]) > 1:
                for key in allPos[i]:
                    del vectors[key]
            
    return len(vectors)

if __name__ == "__main__":
    main()