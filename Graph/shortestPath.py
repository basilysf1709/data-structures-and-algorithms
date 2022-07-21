# Breadth first is better because depth first might go in the wrong direction
# Linear Complexity

from typing import List

def buildGraph(edges: List[List[int]]) -> dict:
    graph = dict()
    for edge in edges:
        a, b = edge[0], edge[1]
        if not a in graph: graph[a] = []
        if not b in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def shortestPath(edges: List[List[int]], src: str, dst: str) -> int:
    graph = buildGraph(edges)
    queue, visited = [[src, 0]], set()
    visited.add(src)
    while len(queue) > 0:
        curr = queue.pop(0)
        node, distance = curr[0], curr[1]
        if node == dst: return distance
        for neighbour in graph[node]:
            if not neighbour in visited:
                visited.add(neighbour)
                queue.append([neighbour, distance + 1])
    return -1
edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v'],
]

print(shortestPath(edges, 'w', 'z'))