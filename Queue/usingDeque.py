from collections import deque

data = deque()
data.append("Basil")
data.append("Ahmed")
data.append("Iqbal")
data.append("Jakob")
data.append("Aliza")
data.popleft() # dequeue operation
data.pop() # removing the first element from the stack
print(data)