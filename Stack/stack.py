# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from typing import List

def printStack(nums: List[int]) -> None:
    for i in range(len(nums) - 1, -1, -1):
        print("[" + str(nums[i]) + "]")
    print()


# Basic LIFO principle displayed in stacks.
# List stack operations is O(n)
data = [] # list
print("Appending 10 to the stack: ")
data.append(10)
printStack(data)
print("Appending 15 to the stack: ")
data.append(15)
printStack(data)
print("Appending 20 to the stack: ")
data.append(20)
printStack(data)
print("Appending 25 to the stack: ")
data.append(25)
printStack(data)
print("Popping from the stack: ")
data.pop()
printStack(data)
print("Popping from the stack: ")
data.pop()
printStack(data)

