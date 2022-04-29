# insertNode(Node head, int data) {
#     if head == None {
#         head = new Node()
#         head.data = data
#         return head
#     }
#     if ( head.data < data) {
#         head.right = insertNode(head.right, data)
#     }
#     head.left = insertNode(head.left, data)

#     return head
# }

# inserting a node in a tree and returning the head