# Queue implementation
# Time: O(n), Given Add and remove O(1)
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

def iterativeBreadthFirstValues(root: Node) -> List[int]:
    if not root: return []
    result, queue = [], [root]
    while len(queue) > 0:
        curr = queue.pop(0)
        result.append(curr.data)
        if curr.left: queue.append(curr.left)
        if curr.right: queue.append(curr.right)
    return result

def bfs(root: Node, target: str) -> bool:
    if not root: return False
    queue = [root]
    while len(queue) > 0:
        curr = queue.pop(0)
        if target == curr.data: return True
        if curr.left: queue.append(curr.left)
        if curr.right: queue.append(curr.right)
    return False

# root = None
# root = Node(1)
# root.left = Node(2)
# root.left.left = Node(4)
# root.left.left.left = Node(5)
# root.left.left.right = Node(100)
# root.left.left.right.left = Node(101)
# root.left.left.right.right = Node(102)
# root.left.left.right.left.left = Node(11)

root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.right = Node('f')

print('Iterative Breadth First Values: ' + str(iterativeBreadthFirstValues(root)))
print('Recursive Breadth First Values: Recursion doesn\'t work properly as recursion is a stack-related concept')

check = input("Search for? ")
print("Is " + check + " found?: " + str(bfs(root, check)))