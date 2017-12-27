import math
def main():

    puzzleInput = open("python/day23.txt", "r").read()

    # Part 1
    # assert(part1("") == 0)
    print(part1(puzzleInput))
    
    # Part 2
    # assert(part2("") == 0)
    print(part2(puzzleInput))

def part1(puzzleInput):

    puzzleInput = puzzleInput.split("\n")
    registers = {}
    instructionPosition = 0

    count = 0
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
        elif instruction[0] == "sub":
            registers[instruction[1]] = registers.get(instruction[1],0) - secondArg
        elif instruction[0] == "mul":
            count += 1
            registers[instruction[1]] = registers.get(instruction[1],0) * secondArg
        elif instruction[0] == "jnz":
            if instruction[1].isalpha():
                if (registers.get(instruction[1],0)) != 0:
                    instructionPosition += (secondArg - 1)
            else:
                if instruction[1] != 0:
                    instructionPosition += (secondArg - 1)

        instructionPosition += 1

    return count 

def isPrime(a):

    x = True 
    for i in range(2, int(math.sqrt(a))):
       if a%i == 0:
           x = False
           break

    return x 

def part2(puzzleInput):

    puzzleInput = puzzleInput.split("\n")
    registers = {}
    registers["a"] = 1
    instructionPosition = 0

    count = 0
    second = 0
    while True:
        # Validate still in array
        if (instructionPosition >= len(puzzleInput) or instructionPosition < 0):
            break
        # define instruction parts
        instruction = puzzleInput[instructionPosition].split(" ")

        # Skip two inner loops
        if instructionPosition == 17:# and count < 18:
            registers['e'] = registers['b']
            if notPrime(registers['b']) == True:
                registers['f'] = 0
        if instructionPosition == 21:
            registers['d'] = registers['b']

        # Convert second arg to int if required
        if (len(instruction) > 2):
            if (instruction[2].isalpha()):
                secondArg = int(registers.get(instruction[2], 0))
            else:
                secondArg = int(instruction[2])
        # Handle insructions
        if instruction[0] == "set":
            registers[instruction[1]] = secondArg
        elif instruction[0] == "sub":
            registers[instruction[1]] = registers.get(instruction[1],0) - secondArg
        elif instruction[0] == "mul":
            registers[instruction[1]] = registers.get(instruction[1],0) * secondArg
        elif instruction[0] == "jnz":
            if instruction[1].isalpha():
                if (registers.get(instruction[1],0)) != 0:
                    instructionPosition += (secondArg - 1)
            else:
                if instruction[1] != 0:
                    instructionPosition += (secondArg - 1)

        instructionPosition += 1

    return registers['h']
 
def notPrime(a):

    for i in range(2, a):
        if a%i == 0:
            return True
    return False

if __name__ == "__main__":
    main()