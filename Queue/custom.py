class Queue:
    def __init__(self):
        self._data = []
    def enqueue(self, data):
        self._data.append(data)
    def dequeue(self):
        return self._data.pop(0)
    def print(self):
        for i in range(len(self._data) - 1, -1, -1):
            print("[" + str(self._data[i]) + "]")
        print()

print("Some enqueue operations")
queue = Queue()
queue.enqueue([1, 2, 3])
queue.enqueue([1, 2])
queue.enqueue([2, 3])
queue.enqueue([1, 3])

queue.print()
print("Dequeue")
queue.dequeue()
queue.print()