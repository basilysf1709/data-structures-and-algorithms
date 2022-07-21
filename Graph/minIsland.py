from typing import List
import sys

# Time complexity: O(rows * columns)
# Space complexity: O(rows * columns)

def minIsland(grid: List[List[str]]) -> int:
    minimum, visited = sys.maxsize, set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = exploreSize(grid, r, c, visited)
            if size > 0: minimum = min(minimum, size)
    return minimum

def exploreSize(grid: List[List[str]], r: int, c: int, visited: set) -> int:
    rowInbounds, columnInbounds = 0 <= r and r < len(grid), 0 <= c and c < len(grid[0])
    if not rowInbounds or not columnInbounds: return 0
    if grid[r][c] == 'W': return 0
    pos = str(r) + ',' + str(c)
    if pos in visited: return 0
    visited.add(pos)

    size = 1
    size += exploreSize(grid, r - 1, c, visited)
    size += exploreSize(grid, r + 1, c, visited)
    size += exploreSize(grid, r, c + 1, visited)
    size += exploreSize(grid, r, c - 1, visited)

    return size


grid = [
    ['W', 'L', 'L', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['W', 'L', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'W', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'L', 'L', 'L', 'W'],
    ['L', 'L', 'W', 'L', 'W'],
    ['L', 'L', 'W', 'W', 'L'],

]

print(minIsland(grid))