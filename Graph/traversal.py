# Depth First : Stack

def dfTraversalPrint(graph: dict, start: str) -> None:
    stack = [start]
    while len(stack) > 0:
        curr = stack.pop()
        print(curr)
        for neighbour in graph[curr]:
            stack.append(neighbour)

def dfTraversalRecursivePrint(graph: dict, start: str) -> None:
    print(start)
    # no base case because loop doesn't enter when the the nodes dont have a neighbour
    for neighbour in graph[start]:
        dfTraversalRecursivePrint(graph, neighbour)


# only iterative list
def bfTraversalPrint(graph: dict, start: str) -> None:
    queue = [start]
    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr)
        for neighbour in graph[curr]:
            queue.append(neighbour)

graph1 = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

graph2 = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# dfTraversalPrint(graph1, 'a')
# print()
# dfTraversalPrint(graph2, 'a')
# print()
# dfTraversalRecursivePrint(graph1, 'a')
# print()
# dfTraversalRecursivePrint(graph2, 'a')

bfTraversalPrint(graph1, 'a')
print()
bfTraversalPrint(graph2, 'a')