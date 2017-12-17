def main():

    puzzleInput = open("python/day16.txt", "r").read()

    # Part 1
    # assert(part1("s1,x3/4,pe/b", "abcde") == "baedc")
    # print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    print(part2(puzzleInput, "abcdefghijklmnop"))

def part1(puzzleInput, programs):

    instructions = puzzleInput.split(",")

    programs = list(programs) #list("abcdefghijklmnop")
    for i in instructions:
        instructionType = i[0]
        # Spin
        if instructionType == "s":
            temp = []
            temp.extend(programs[-int(i[1:]):])
            temp.extend(programs[0:-int(i[1:])])
            programs = temp[:]
        # Exchange
        elif instructionType == "x":
            first = int(i[1:].split("/")[0])
            sec = int(i[1:].split("/")[1])
            stored = programs[first]
            programs[first] = programs[sec]
            programs[sec] = stored

        # Partner
        elif instructionType == "p":
            first = programs.index(i[1:].split("/")[0])
            sec = programs.index(i[1:].split("/")[1])
            stored = programs[first]
            programs[first] = programs[sec]
            programs[sec] = stored
    # print("".join(programs))

    return "".join(programs)

def part2(puzzleInput, programs):

    currentLineUp = list(programs) 
    seen = set()
    for i in range(0, 10):
        newOrder = part1(puzzleInput, currentLineUp)
        if newOrder in seen:
            print(newOrder, i)
        else:
            seen.add(newOrder)

        currentLineUp = newOrder

    return currentLineUp 


if __name__ == "__main__":
    main()