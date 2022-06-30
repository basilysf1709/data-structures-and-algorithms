from heapq import heapify, heappush, heappop
  
# Creating empty heap
heap = []
heapify(heap)
  
# Adding items to the heap using heappush function
heappush(heap, 10)
heappush(heap, 30)
heappush(heap, 20)
heappush(heap, 400)

# printing the value of minimum element
print("Head value of heap : "+str(heap[0]))
  
# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(i, end = ' ')
print("\n")
  
element = heappop(heap)
  
# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(i, end = ' ')

#insertion: O(n * log(n))
#heap sort: delete and add it at the end
#^ heap sort, time complexity: O(n * log(n))
#heapify: direction is different from normal create heap
# ^ downward and from right-direction => O(n)

## Larger number -> higher priority: max heap
## Smaller number -> higher priority: min heap
## Heap is the best data structure for priority queues because it takes O(log(n)) time. 
## Arrays take O(n) in insertion, deletion, etc