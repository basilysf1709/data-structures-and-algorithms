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

# Time Complexity: O(n)
# Space Complexity: O(n)
# Recursive Depth First 
def sumTree(root: Node) -> int:
    if not root: return 0
    return root.data + sumTree(root.left) + sumTree(root.right)

# Time Complexity: O(n)
# Space Complexity: O(n)
# Iterative Breadth First
def treeSum(root: Node) -> int:
    if not root: return 0
    sum, queue = 0, [root]
    while len(queue) > 0:
        curr = queue.pop(0)
        sum += curr.data
        if curr.left: queue.append(curr.left)
        if curr.right: queue.append(curr.right)
    return sum

# root = None
root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.left = Node(4)
root.left.left.right = Node(5)
root.left.left.right.left = Node(6)
root.left.left.right.right = Node(7)
root.left.left.right.left.left = Node(8)

# sum = 0
# for i in range(1, 9):
#     sum += i
# print("The sum is: " + str(sum))

print("The sum is (Recursive Depth First): " + str(sumTree(root)))
print("The sum is (Iterative Breadth First): " + str(treeSum(root)))