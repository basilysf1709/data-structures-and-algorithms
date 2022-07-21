from typing import List

# check when revising
# Adjacency List
def buildGraph(edges: List[List[int]]) -> dict:
    graph = dict()
    for edge in edges:
        a, b = edge[0], edge[1]
        if not a in graph: graph[a] = []
        if not b in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

# main function
def undirectedPath(edges: List[List[int]], nodeA: str, nodeB: str) -> bool:
    graph = buildGraph(edges)
    return hasPath(graph, nodeA, nodeB, set())

# checking has path
def hasPath(graph: dict, src: str, dst: str, visited: set) -> bool:
    if src == dst: return True
    if src in visited: return False

    visited.add(src)

    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dst, visited) == True:
            return True
    return False

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print(undirectedPath(edges, 'i', 'n'))
