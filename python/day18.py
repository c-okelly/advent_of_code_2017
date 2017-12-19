def main():

    puzzleInput = open("python/day18.txt", "r").read()

    # Part 1
    assert(part1("""set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2""") == 4)
    print(part1(puzzleInput))
    
    # Part 2
    assert(part2("""snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d""") == 3)
    print(part2(puzzleInput))

def part1(puzzleInput):

    puzzleInput = puzzleInput.split("\n")
    registers = {}
    lastPlayed = 0
    recoverdSound = 0
    instructionPosition = 0

    while True:
        # Validate still in array
        if (instructionPosition >= len(puzzleInput) or instructionPosition < 0):
            break
        # define instruction parts
        instruction = puzzleInput[instructionPosition].split(" ")
        # print(instruction)
        # Convert second arg to int if required
        if (len(instruction) > 2):
            if (instruction[2].isalpha()):
                secondArg = int(registers.get(instruction[2], 0))
            else:
                secondArg = int(instruction[2])

        # Handle insructions
        if instruction[0] == "set":
            registers[instruction[1]] = secondArg
        elif instruction[0] == "add":
            registers[instruction[1]] = registers.get(instruction[1],0) + secondArg
        elif instruction[0] == "mul":
            registers[instruction[1]] = registers.get(instruction[1],0) * secondArg
        elif instruction[0] == "mod":
            registers[instruction[1]] = registers.get(instruction[1],0) % secondArg
        elif instruction[0] == "snd":
            if registers[instruction[1]] > 0:
                lastPlayed = registers[instruction[1]]
        elif instruction[0] == "rcv":
            if (registers.get(instruction[1],0)) > 0:
                recoverdSound = lastPlayed
                break
        elif instruction[0] == "jgz":
            if (registers.get(instruction[1],0)) > 0:
                instructionPosition += secondArg - 1

        instructionPosition += 1

    return recoverdSound

def part2(puzzleInput):

    puzzleInput = puzzleInput.split("\n")
    groupRegisters = [{"p":0}, {"p":1}]
    lastPlayed = [0, 0]
    waitingOrTerminated = [False, False]
    messageQeue = [[], []]
    iPosition = [0,0]

    messagesACount = 0

    while True:
        # Run both lists
        if (waitingOrTerminated[0] == True and waitingOrTerminated[1] == True):
            break
        # print(waitingOrTerminated, iPosition, puzzleInput[iPosition[0]], puzzleInput[iPosition[1]])
        # print(groupRegisters)
        for program in range(0,2):
            # Check if both waiting / terminated
            if (waitingOrTerminated[0] == True and waitingOrTerminated[1] == True):
                break
            # Validate still in array
            # print(iPosition[program])
            if (iPosition[program] >= len(puzzleInput) or iPosition[program] < 0):
                waitingOrTerminated[program] = True
                continue
            # Check if new message. If not move to next iteration
            if waitingOrTerminated[program] == True:
                if len(messageQeue[program]) == 0:
                    continue
                else:
                    waitingOrTerminated[program] = False

            # define instruction parts
            registers = groupRegisters[program]
            instructionPosition = iPosition[program]
            instruction = puzzleInput[instructionPosition].split(" ")

            # Convert second arg to int if required
            if (len(instruction) > 2):
                if (instruction[2].isalpha()):
                    secondArg = int(registers.get(instruction[2], 0))
                else:
                    secondArg = int(instruction[2])

            # Handle insructions
            if instruction[0] == "set":
                registers[instruction[1]] = secondArg
            elif instruction[0] == "add":
                registers[instruction[1]] = registers.get(instruction[1],0) + secondArg
            elif instruction[0] == "mul":
                registers[instruction[1]] = registers.get(instruction[1],0) * secondArg
            elif instruction[0] == "mod":
                registers[instruction[1]] = registers.get(instruction[1],0) % secondArg

            elif instruction[0] == "jgz":
                if instruction[1].isalpha():
                    if (registers.get(instruction[1], 0)) > 0:
                        instructionPosition += secondArg - 1
                else:
                    if int(instruction[1]) > 0:
                        instructionPosition += secondArg - 1

            # Send recieve
            elif instruction[0] == "snd":
                # if int(instruction[1]) > 0:
                value = instruction[1]
                if (instruction[1].isalpha()):
                    value = registers.get(instruction[1],0)
                messageQeue[(program+1) % 2].append(value)
                # lastPlayed = registers[instruction[1]]
                # Count prog 1 messages
                if program == 1:
                    messagesACount += 1

            elif instruction[0] == "rcv":
                currQeue = messageQeue[program]
                # print("cur", currQeue)
                if len(currQeue) == 0:
                    waitingOrTerminated[program] = True
                    instructionPosition -= 1
                else:
                    item = messageQeue[program].pop(0)
                    registers[instruction[1]] = item


            iPosition[program] = instructionPosition + 1

    return messagesACount 

if __name__ == "__main__":
    main()