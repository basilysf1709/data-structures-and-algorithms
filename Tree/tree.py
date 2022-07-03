# binary tress:
# at most 2 children
# exactly 1 root
# exactly 1 path b/w root and any node
# empty tree has no nodes



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return 'Node: ' + str(self.data)
    def printData(self):
        print(str(self.left) + " " + str(self.right))
    
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

a.printData()
b.printData()
c.printData()