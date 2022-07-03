import sys
from typing import List

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # print classes
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return 'Node: ' + str(self.data) + ', Left: ' + str(self.left) + ', Right: ' + str(self.right)


# Depth First Recursive
# Time complexity: O(n)
# Space Completxity: O(n)
def minTree(root: Node) -> int:
    if not root: return sys.maxsize
    leftMin = minTree(root.left)
    rightMin = minTree(root.right)
    return min(root.data, leftMin, rightMin)

# Breadth First Iterative
# Time complexity: O(n)
# Space Completxity: O(n)
def minTreeBFS(root: Node) -> int:
    queue = [root]
    minimum = sys.maxsize # Python3's largest integer is sys.maxsize, Python2's largest is sys.maxint
    while len(queue) > 0:
        curr = queue.pop(0)
        if curr.data < minimum: minimum = curr.data
        if curr.left: queue.append(curr.left)
        if curr.right: queue.append(curr.right)
    return minimum

# Depth First Iterative
# Time complexity: O(n)
# Space Completxity: O(n)
def minTreeDFS(root: Node) -> int:
    stack = [root]
    minimum = sys.maxsize # Python3's largest integer is sys.maxsize, Python2's largest is sys.maxint
    while len(stack) > 0:
        curr = stack.pop()
        if curr.data < minimum: minimum = curr.data
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    return minimum

root = Node(1231241)
root.left = Node(1002)
root.left.left = Node(2341)
root.left.left.left = Node(1231)
root.left.left.right = Node(123123)
root.left.left.right.left = Node(1012311)
root.left.left.right.right = Node(121231000)
root.left.left.right.left.left = Node(123541)

print("The minimum value is (Recursive DF Min Value): " + str(minTree(root)))
print("The minimum value is (Iterative BF Min Value): " + str(minTreeBFS(root)))
print("The minimum value is (Iterative DF Min Value): " + str(minTreeDFS(root)))