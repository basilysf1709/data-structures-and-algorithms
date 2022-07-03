from typing import List
import sys

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

# Depth First Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def maxRootToLeafSum(root: Node) -> int:
    if not root: return -1 * sys.maxsize
    if not root.left and not root.right: return root.data # check if == None is important here
    return root.data + max(maxRootToLeafSum(root.left), maxRootToLeafSum(root.right))

# root = None
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(4)
root.left.left.right = Node(5)
root.left.left.right.left = Node(6)
root.left.left.right.right = Node(7)
root.left.left.right.left.left = Node(8)

print("The max sum is: " + str(maxRootToLeafSum(root)))