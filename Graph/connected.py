# Time: O(edges)
# Space: O(nodes)

def connectedComponents(graph: dict) -> int:
    visited, count = set(), 0
    for node in graph:
        if explore(graph, node, visited) == True:
            count += 1
    return count

def explore(graph: dict, node: int, visited: set) -> bool:
    if node in visited: return False
    visited.add(node)
    for neighbour in graph[node]:
        explore(graph, neighbour, visited)
    
    return True



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

print(connectedComponents(graph))
print(connectedComponents(graph1))