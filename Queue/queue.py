# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from typing import List

def printQueue(nums: List[int]) -> None:
    for i in range(len(nums) - 1, -1, -1):
        print("[" + str(nums[i]) + "]")
    print()


# Basic FIFO principle displayed in queues.
# Enqueue and Dequeue operations
# List enqueue and dequeue operations is O(n)
data = [] # list
print("Enqueue 10: ")
data.append(10)
printQueue(data)
print("Enqueue 15: ")
data.append(15)
printQueue(data)
print("Enqueue 20: ")
data.append(20)
printQueue(data)
print("Enqueue 25: ")
data.append(25)
printQueue(data)
print("Dequeue: ")
data.pop(0) # FIFO principle
printQueue(data)
print("Dequeue: ")
data.pop(0) # FIFO principle
printQueue(data)


# In Python data.pop(0) returns the element that is popped
# Example: element = data.pop(0). print(element) will print
# element will be the element popped from data