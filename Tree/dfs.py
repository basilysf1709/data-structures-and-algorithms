# Stack implementation
# Time: O(n)
# Space: O(n)

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
  
def iterativeDepthFirstValues(root: Node) -> List[int]:
    if not root: return []
    result, stack = [], [root]
    while len(stack) > 0:
        curr = stack.pop()
        result.append(curr.data)
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    return result

def iterativeDFS(root: Node, target: int) -> bool:
    if not root: return []
    stack = [root]
    while len(stack) > 0:
        curr = stack.pop()
        if curr.data == target: return True
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
    return False

def recursiveDepthFirstValues(root: Node) -> List[int]:
    if not root: return []
    leftValues = recursiveDepthFirstValues(root.left)
    rightValues = recursiveDepthFirstValues(root.right)
    return [root.data] + leftValues + rightValues

def recursiveDFS(root: Node, target: int) -> bool:
    if not root: return False
    if root.data == target: return True
    return recursiveDFS(root.left, target) or recursiveDFS(root.right, target)

    
 
# root is None, check this condition for coding problems
# root = None

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.left.left = Node(5)
root.left.left.right = Node(100)
root.left.left.right.left = Node(101)
root.left.left.right.right = Node(102)
root.left.left.right.left.left = Node(11)

print('Iterative Depth First Values: ' + str(iterativeDepthFirstValues(root)))
print('Recursive Depth First Values: ' + str(recursiveDepthFirstValues(root)))
check = input("Search for? ")
print("Is " + check + " found? (Iterative DFS): " + str(iterativeDFS(root, int(check))))
print("Is " + check + " found? (Recursive DFS): " + str(recursiveDFS(root, int(check))))