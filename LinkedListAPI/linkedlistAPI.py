class LinkedList:

  def __init__(self, data, next = None):
    self.data = data
    self.next = None
  
  def print(self, head):
    if head is None:
      print("Linked list is empty")
    else:
      temp = head
      while head:
        print("[" + str(head.data) + "]" + '-->', end="")
        head = head.next
      print("[None]")

  def insert(self, head, data):
    if head == None:
      Node = LinkedList(data, None)
    else:
      while head.next:
        head = head.next
      Node = LinkedList(data, None)
      head.next = Node

  def getLength(self, head):
    count = 0
    while head:
      head = head.next
      count += 1
    return count

  def removeNode(self, head, index):
    if index >= head.getLength(head):
      print("Out of bounds")
      return
    if index == 0:
      return head.next
    else:
      count = 0
      temp = head
      while temp:
        if index - 1 == count:
          temp.next = temp.next.next
        count += 1
        temp = temp.next
      return head

  def reverseList(self, head):
    temp, prev = head, None
    while temp: 
      nxt = temp.next
      temp.next = prev
      prev = temp
      temp = nxt
    return prev
  
  def insertAtStart(self, head, data):
    if head == None:
      return LinkedList(data, None)
    Node = LinkedList(data, head)
    Node.next = head
    return Node

  def insertAtIndex(self, head, data, index):
    if index - 1 > head.getLength(head):
      print("Out of bounds")
      return
    
    if index == 0:
      head = head.insertAtStart(head, data)
      return head

    elif index - 1 == head.getLength(head):
      head.insert(head, data)
      return head

    else:
      temp = head
      count = 0
      while temp:
        if count == index - 1:
          Node = LinkedList(data, None)
          Node.next = temp.next
          temp.next = Node
          return head
        temp = temp.next
        count += 1
  
Node = LinkedList(0, None)
print("Before Inserting: ")
Node.print(Node)

Node.insert(Node, 1)
Node.insert(Node, 2)
Node.insert(Node, 3)
Node.insert(Node, 4)
Node.insert(Node, 5)
print("After inserting: ")
Node.print(Node)

print("Length of the Linked list right now: ", end="")
print(Node.getLength(Node))

removeNodeIndex = 2
Node = Node.removeNode(Node, removeNodeIndex)
print("After removing the Node Number " + str(removeNodeIndex))
Node.print(Node)

Node = Node.reverseList(Node)
print("Reversing Linked List: ")
Node.print(Node)

Node = Node.insertAtStart(Node, -1)
print("Inserting at the start of Linked List: ")
Node.print(Node)

index = 0
Node = Node.insertAtIndex(Node, -2, index)
print("Inserting at the index " + str(index) + ":")
Node.print(Node)

index = 8
Node = Node.insertAtIndex(Node, -3, index)
print("Inserting at the index " + str(index) + ":")
Node.print(Node)

index = 4
Node = Node.insertAtIndex(Node, 9, index)
print("Inserting at the index " + str(index) + ":")
Node.print(Node)