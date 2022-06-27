class Stack:
    def __init__(self):
        self._data = []
    def push(self, data):
        self._data.append(data)
    def pop(self):
        return self._data.pop()
    def print(self):
        for i in range(len(self._data) - 1, -1, -1):
            print("[" + str(self._data[i]) + "]")
        print()

print("Some stack operations: ")
stack = Stack()
stack.push([1, 2, 3])
stack.push([1, 2])
stack.push([2, 3])
stack.push([1, 3])

stack.print()
print("Popping off the stack")
stack.pop()
stack.print()
    