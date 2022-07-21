

def connectedComponentsLength(graph: dict) -> int:
    visited, maximum = set(), 0
    for node in graph:
        maximum = max(exploreSize(graph, node, visited), maximum)
    return maximum

def exploreSize(graph: dict, node: int, visited: set) -> int:
    if node in visited: return 0
    visited.add(node)
    size = 1
    for neighbour in graph[node]:
        size += exploreSize(graph, neighbour, visited)
    return size


graph = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1],
}

graph1 = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2],
}

print(connectedComponentsLength(graph))
print(connectedComponentsLength(graph1))
