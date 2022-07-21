# is there a path that exists

# Two ways
# Time complexity: O(edges)
# Space complexity: O(nodes)

# Time complexity: O(nodes ^ 2)
# Space complexity: O(nodes)

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': ['a', 'b', 'c'],
    'a': [],
    'b': [],
    'c': []
}

# Depth First
def hasPath(graph: dict, src: str, dst: str) -> bool:
    if src == dst: return True
    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dst) == True: return True
    return False

# Breadth First
def hasPathBF(graph: dict, src: str, dst: str) -> bool:
    queue = [src]
    while len(queue) > 0:
        curr = queue.pop(0)
        if curr == dst: return True
        for neighbour in graph[curr]:
            queue.append(neighbour)
    return False

print(hasPath(graph, 'f', 'b'))
print(hasPathBF(graph, 'f', 'b'))