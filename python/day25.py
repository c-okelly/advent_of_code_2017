def main():

    testInput = """Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A."""

    assert(part1(testInput) == 3)

    puzzleInput = open("python/day25.txt", "r").read()
    # Part 1 the final one!
    # assert(part1("") == 0)
    print(part1(puzzleInput))
    # test()

def part1(puzzleInput):

    puzzleInput = puzzleInput.split("\n")

    startState = puzzleInput.pop(0).split(" ")[3][0]
    checkSumStep = int(puzzleInput.pop(0).split(" ")[5])
    # puzzleInput.pop(0)
    sections = []
    singleSection = []

    for i in puzzleInput:
        if i == "":
            if len(singleSection) > 0:
                sections.append(singleSection)
            singleSection = []
        else:
            singleSection.append(i)
    sections.append(singleSection)

    states = {}

    # Build sections
    for s in sections:
        # print(s)
        stateName = s.pop(0).split(" ")[2][0]
        # Branch1
        b1Matcher = s.pop(0).strip().split(" ")[5][0]
        b1ValueChange = s.pop(0).strip().split(" ")[4][0]
        if s.pop(0).strip().split(" ")[6] == "right.":
            b1Direction = 1
        else:
            b1Direction = -1
        b1NewState = s.pop(0).strip().split(" ")[4][0]
        # Branch2
        b2Matcher = s.pop(0).strip().split(" ")[5][0]
        b2ValueChange = s.pop(0).strip().split(" ")[4][0]
        if s.pop(0).strip().split(" ")[6] == "right.":
            b2Direction = 1
        else:
            b2Direction = -1
        b2NewState = s.pop(0).strip().split(" ")[4][0]

        state = State(stateName, b1Matcher)
        state.addB1(b1ValueChange, b1Direction, b1NewState)
        state.addB2(b2ValueChange, b2Direction, b2NewState)

        states[stateName] = state

    print(states)
    print()


    # Apply states

    tape = {0: 0}
    position = 0
    stepCount = 0
    currnetState = states.get(startState)
    while stepCount < checkSumStep:

        (position, nextState) = currnetState.applyStep(tape, position)
        currnetState = states[nextState]

        # print(position, currnetState.stateName)
        # print(tape)
        stepCount += 1


    checkSumTotal = 0
    for key in tape.keys():
        checkSumTotal += int(tape[key])


    # print(checkSumTotal)
    # print(tape)

    return checkSumTotal

    
# def part1(puzzleInput):

#     puzzleInput = puzzleInput.split("\n\n")
#     sections = []
#     for i in puzzleInput:
#         if len(i) > 0:
#             sections.append(i.split('\n'))



#     startState = ""
#     checksumAtStep = 0
#     # Build turing machine

#     # Run for x Step

#     #

#     return 0

class State:

    def __init__(self, stateName, b1Matcher):
        self.stateName = stateName
        self.b1Matcher = b1Matcher

    def applyStep(self, tape, position):
        if tape.get(position, 0) == int(self.b1Matcher):
            tape[position] = int(self.b1ValueChange)
            position += self.b1NewDirection
            return (position, self.b1NewState)

        else:
            tape[position] = int(self.b2ValueChange)
            position += self.b2NewDirection
            return (position, self.b2NewState)

    def addB1(self, valueChange, newDirection, newState):
        self.b1ValueChange = valueChange
        self.b1NewDirection = newDirection
        self.b1NewState = newState

    def addB2(self, valueChange, newDirection, newState):
        self.b2ValueChange = valueChange
        self.b2NewDirection = newDirection
        self.b2NewState = newState
    
    def __repr__(self):
        return "\nName: " + self.stateName + ". First branch match: " + self.b1Matcher + ".\n Branch 1: " + str(self.b1ValueChange) + ". " + str(self.b1NewDirection) + ". " + str(self.b1NewState) + ".\n Branch 2: " + str(self.b2ValueChange) + ". " + str(self.b2NewDirection) + ". " + str(self.b2NewState)

if __name__ == "__main__":
    main()