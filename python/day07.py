from collections import Counter

def main():

    puzzleInput = open("python/day07.txt", "r").read()

    # Part 1
    assert(part1("""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""") == "tknk")
    print(part1(puzzleInput))
    
    # Part 2
    assert(part2("""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""") == 60)
    print(part2(puzzleInput))

def part1(puzzleInput):

    programs = puzzleInput.split("\n")

    nodes = set()
    for i in puzzleInput.split("\n"):
        node = i.split()[0]
        nodes.add(node)

    for i in puzzleInput.split("\n"):
        children = i.split("->")
        if (len(children) > 1):
            children = children[1].split(",")
            for child in children:
                nodes.remove(child.strip())

    return nodes.pop()

class Program:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
        self.totalWeight = 0
        self.totalWeightSet = False
    
    def addChild(self, child):
        self.children.append(child)

    def calculateWeight(self):
        if (self.totalWeightSet):
            return self.totalWeight
        weight = self.weight
        for child in self.children:
            weight += child.calculateWeight()
        self.totalWeight = weight
        self.totalWeightSet = True
        return weight

    def getChildren(self):
        return self.children

    def __repr__(self):
        childNames = [x.name for x in self.children]
        return "Program => Name: " + self.name + ". Weight: " + str(self.weight) + " Children " + str(childNames) + ". Total weight: " + str(self.totalWeight) 

def part2(puzzleInput):

    tree = {}
    programInfo = puzzleInput.split("\n")
    # Add nodes with no children / parents
    for i in programInfo:
        row = i.split()
        name = row[0]
        weight = int(row[1].replace("(","").replace(")",""))
        tree[name] = Program(name, weight)

    for i in programInfo:
        row = i.split("->")
        if(len(row) > 1):
            name = row[0].split()[0]
            currentNode = tree.get(name)
            children = row[1].strip().split(",")


            for child in children:
                child = tree.get(child.strip())
                currentNode.addChild(child)

    rootNode = tree.get(part1(puzzleInput))
    rootNode.calculateWeight()

    oddNodeWeight = findOddNodeOut(rootNode, tree)

    return oddNodeWeight

def findOddNodeOut(currentNode, tree):

    currentOddNode = currentNode
    currentParent = currentOddNode
    while True:
        # print(currentOddNode)
        children = currentOddNode.getChildren()
        c = Counter()
        weightToName = {}
        for child in children:
            c[child.calculateWeight()] += 1
            weightToName[child.calculateWeight()] = child.name
        # If current node is the ones that needs weight changed
        if (len(c.keys()) == 1):
            # print(currentOddNode)
            break

        currentParent = currentOddNode
        currentOddNode = tree.get(weightToName.get(c.most_common()[-1][0]))
        # print(currentOddNode.name, currentParent.name)

    oddChildren = currentParent.getChildren()
    c = Counter()
    for i in oddChildren:
        c[i.calculateWeight()] += 1

    adjustWeight = c.most_common()[0][0] - c.most_common()[-1][0]

    # print(oddChildren)
    # print(adjustWeight, currentOddNode.weight)
    return int(currentOddNode.weight) + adjustWeight

if __name__ == "__main__":
    main()