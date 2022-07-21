# is there a path that exists

# Two ways
# Time complexity: O(edges)
# Space complexity: O(nodes)

# Time complexity: O(nodes ^ 2)
# Space complexity: O(nodes)

graph1 = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

def hasPath(graph: dict, src: str, dst: str) -> bool:
    if src == dst: return True
    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dst) == True: return True
    return False

print(hasPath(graph1, 'f', 'k '))