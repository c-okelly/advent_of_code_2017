def main():

    puzzleInput = open("python/day25.txt", "r").read()

    # Part 1 the final one!
    assert(part1("") == 0)
    print(part1(puzzleInput))
    
def part1(puzzleInput):

    puzzleInput = puzzleInput.split("\n\n")
    sections = []
    for i in puzzleInput:
        if len(i) > 0:
            sections.append(i.split('\n'))



    startState = ""
    checksumAtStep = 0
    # Build turing machine

    # Run for x Step

    #

    return 0

class State:

    def __init__(self, stateID, step1, step2):
        self.tape = {0: 0}
        self.currentPosition = 0

        self.stateID = stateID
        self.step1 = step1
        self.step2 = step2

    def __str__(self):
        return "State: %s, current position is %s. \nStep 1 is %s. \nStep 2 is %s.  \nCurrent tape is: %s" % (self.stateID, self.currentPosition, self.step1, self.step2, self.tape)

class Step:

    def __init__(self, newValue, movementDirection, nextState):
        self.newValue = newValue
        self.movementDirection = movementDirection
        self.nextState = nextState


    def __str__(self):
        return "Step: change current val to %s move position to %s and move to next state %s" % (self.newValue, self.movementDirection, self.nextState)
        



if __name__ == "__main__":
    # main()
    a = State("A", Step(0,0,0), Step(0,0,0))
    print(a)