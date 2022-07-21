from typing import List

# check this later
# not tested
# Time complexity: O(rows * columns)
# Space complexity: O(rows * columns) [because of visited set]

def islandCount(grid: List[List[str]]) -> int:
    visited, count = set(), 0
    # convert this to a numbered loop and not value
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited) == True:
                count += 1
    return count

def explore(grid: List[List[str]], r: int, c: int, visited: set) -> bool:
    rowInbounds = 0 <= r and r < len(grid)
    columnInbounds = 0 <= c and c < len(grid[0])
    if not rowInbounds or not columnInbounds: return False
    if grid[r][c] == 'W': return False
    pos = str(r) + ',' + str(c)
    if pos in visited: return False
    visited.add(pos)

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True

island = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]


print(islandCount(island))