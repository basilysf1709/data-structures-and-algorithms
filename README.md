# Data Structures & Algorithms

# Data Structures
1. Arrays
2. Linked Lists (Single & Double)
3. Trees (Binary Trees, Heaps, etc)
4. Hash Maps
5. Graphs
6. Stacks/ Queues

# Algorithms
1. Sorting
2. Recursive Algorithms (Dynamic Programming)

# Other Important things:
1. Time Complexity Concepts
2. Space Complexity Concepts

# Recursion 
1. Divide the problem into smaller sub problems
2. Specify the base condition to stop the recursion
3. Breakdown:
Fact():
if: base case
else: functionality
=> Elegance and code modularity
=> Memoization: Important (Can reduce time complexity)
=> Works well with graphs and trees
=> Cons: Memory Overhead

=> Important : Call Stack:
[Task 1]
[Task 2]
[Task 3]
[Task 4]
to
[Task 2]
[Task 3]
[Task 4]
=>
[Task 3]
[Task 4]
=>
[Task 4]
=> Empty
## Memoization and Caching
An optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again.
## Depth First Search (algorithm example for graphs)
Definition: Depth first Search or Depth first traversal is a recursive algorithm for searching all the vertices of a graph or tree data structure. Traversal means visiting all the nodes of a graph.
Roughly:
     base: if node == null then false
     if node.val == goal then True
     get all the neighbors and checks if it has been visited or not
     if it has continue else just do dfs recursively on the graph path until found or every possibility has ended
     else return False
## Explore Tail - Call Recursion Optimization
=> freeCodeCamp.org: https://youtu.be/IJDJ0kBx2LM
## LeetCode 238: Product of Array Except Self:
Sol) Left and Right Products 
     Left: [1,2,3,4] => [1,1,2,6] 
     Right: [1,2,3,4] => [24,12,4,1]
     Output: Left * Right => [24,12,8,6]
     Note: Left Index, loop is 1 to 3(1,2,3) and Right Index, loop is 2 to 0(2,1,0)
## LeetCode 53: Maximum Sum Subarray:
Sol) Kadane's Algorithm
     Eg: [-2,1,-3,4,-1,2,1,-5,4]
     => loopCounter from 0 to i - 1
     => set max and current to index 0, "-2" in this case
     => current = current + arr[loopCounter + 1]
     => if current < arr[loopCounter + 1], then current equals arr[loopCounter + 1]
     => if max < current, max = current
## LeetCode 152: Maximum Product Subarray
Sol) Kadane's Algorithm with currMin and currMax
     => initialize max as nums[0] for single array cases
     => nums[i] = 1, then currMin and currMax = 1
     => currMax = max of(n * currMax, n * currMin, n)
     => currMin = min of(n * currMax, n * currMin, n), (Careful: should be of this iteration, take a tmp at the start for currMax)
     => max = max of(currMax, max)
## LeetCode 371: Sum of Two Integers without +/-
Sol) 
Algorithm by example:
     =>      1011 (11)
     => (xor)1001 (9)
     -----------------
     =>      0010 (new a value)
     =>           1011 (11)
     => (and << 1)1001 (9) [note: do and gate and shift 1]
     ---------------------
     =>          10010 (new b value)
     => Do the same operation again: a = a ^ b, b = (a & b) << 1, till b = 0. 
     => Answer: 10100(20) [Note: b-value becomes 0 if we don't have a carry, otherwise it changes]

## LeetCode 242: Valid Anagram
Sol) Algorithm:
     => Convert both to character arrays
     => Check if length is equal first, then
     => Sort them, and then check if each character is equal => arr[i] = arr1[i]
## LeetCode 153: Find Minimum in Rotated Sorted Array
Sol) Use Arrays.sort(nums) => return nums[0], [Note: Check how sort works]
## LeetCode 39: Search in Rotated Sorted Array
Sol) Do it normally, [Note: Check Merge Sort]
## LeetCode 11: Container With Most Water
Sol) Algorithm: Two Pointer Technique [Note: if equal, discard either height but be consistent]
     => [1,8,6,2,5,4,8,3,7] => Area = 1 * (pointer2 - pointer1) = 1 * 8 = 8
     => discard smaller height => Area = 7 * (pointer2 - pointer1) = 7 * 7 = **49**
     => discard smaller height => Area = 3 * (pointer2 - pointer1) = 3 * 6 = 18
     => discard smaller height => Area = 8 * (pointer2 - pointer1) = 8 * 5 = 40
     => discard smaller height => Area = 4 * (pointer2 - pointer1) = 4 * 4 = 16
     => discard smaller height => Area = 5 * (pointer2 - pointer1) = 5 * 3 = 15
     => discard smaller height => Area = 2 * (pointer2 - pointer1) = 2 * 2 = 4
     => discard smaller height => Area = 6 * (pointer2 - pointer1) = 6 * 1 = 6
     => 49 is the largest area
## LeetCode 15: 3sum:
Sol) Algorithm: Brute Force => Make three loops and check the sum for each elements 3 times. Continue the loop when indices are equal to one another.
Algorithm: Pointer technique
=> Go through every element by making a loop
=> Make a second loop and then select a left pointer
and a right pointer
=> Example: [-1,0,1,3,-1,-4]
=> Sort: [-4,-1,-1,-,1,3]
=> Select -1 first, then loop from index[1] to index[length]
=> if sum < 0 increase lp by 1
=> if sum > 0 decrease rp by 1
=> else append to list if already not in the list
=> return list
## LeetCode 268. Missing Number:
=> sort the array
=> if i does not equal to num[i], return i
=> else just return len(nums) => example [0,1] is [0,n] where n = 2.
=> since 2 is equal to len(nums)
=> Other solution: Sum of [0,n] - sum of array
=> One more solution: Using xor gate. T
=> 5 xor 5 = 0. Similarly, 5 xor 5 xor 3 = 3
## LeetCode 191. Number of 1 Bits:
=> Use the bin function to convert to a String
=> Use the count function to count the occurrences of '1'
=> To convert to Binary:
=> Example: 11 (Keep doing 11/2, 5/2 and so on)
=> 11 % 2 = 1
=> 5 % 2 = 1
=> 2 % 2 = 0
=> 1 % 2 = 1
=> Reverse the string to get: 1011
## LeetCode 338. Counting Bits:
=> Make an empty list
=> make an array using range (0, n + 1)
=> Count the number of 1s using the bin() function
=> Make sure to understand how bin function works
=> add the count of 1s to the empty list 
=> Return the list
## LeetCode 190. Reverse Bits:
=> Convert int to a string using "{:32b}".format(number)
=> Extra exercise: Do the 32 string thing as an exercise
=> Go from 0 to n indices
=> Use the binary formula
=> Example: 101 = 2^0 x 1 + 2^1 x 0 + 2^2 x 1 = 5
=> Since the count starts from the rightmost bit. Sum will be the number of the reversed bit
## LeetCode 322. Coin Change:
Algorithm: Dynamic Programming, DFS
Example tracing: [1,2,5], amount = 11
start with an array:
least[0] = 12
least[1] = 12
least[2] = 12
least[3] = 12
least[4] = 12
least[5] = 12
least[6] = 12
least[7] = 12
least[8] = 12
least[9] = 12
least[10] = 12
least[11] = 12 or 
=> `least[0 to amount] = amount + 1`
start with least[0] = 0 as 0 gives 0 back
loop through 1 to 11 (inclusive)
and then through coins:
First iteration: 
i = 1,
     => c = 1 and minimum of[ least[1] = 12, 1 + least[i - c = 0] ] gives least[1] = 1 + 0 = 1
     => c = 2, loop does not enter as i - c = -1
     => c = 5, loop does not enter as i - c = -4
     => Result: least[1] = 1
Second iteration: 
i = 2,
     => c = 1 and minimum of[ least[2] = 12, 1 + least[i - c = 1] ] gives least[2] = 1 + 1 = 2
     => c = 2, and minimum of[ least[2] = 12, 1 + least[i - c = 0] ] gives least[2] = 1 + 0 = 1
     => c = 5, loop does not enter as i - c = -3
     => Result: least[2] = 1
Third iteration: 
i = 3,
     => c = 1 and minimum of[ least[3] = 12, 1 + least[i - c = 2] ] gives least[3] = 1 + 1 = 2
     => c = 2, and minimum of[ least[3] = 12, 1 + least[i - c = 1] ] gives least[3] = 1 + 1 = 2
     => c = 5, loop does not enter as i - c = -2
     => => Result: least[3] = 2
Fourth iteration: 
i = 4,
     => c = 1 and minimum of[ least[4] = 12, 1 + least[i - c = 3] ] gives least[4] = 1 + 2 = 3
     => c = 2, and minimum of[ least[4] = 12, 1 + least[i - c = 2] ] gives least[4] = 1 + 1 = 2
     => c = 5, loop does not enter as i - c = -1
     => => Result: least[4] = 2
Fifth iteration: 
i = 5,
     => c = 1 and minimum of[ least[5] = 12, 1 + least[i - c = 4] ] gives least[5] = 1 + 2 = 3
     => c = 2, and minimum of[ least[5] = 12, 1 + least[i - c = 3] ] gives least[5] = 1 + 2 = 3
     => c = 5, and minimum of[ least[5] = 12, 1 + least[i - c = 0] ] gives least[5] = 1
     => => Result: least[5] = 1
Sixth iteration: 
i = 6,
     => c = 1 and minimum of[ least[6] = 12, 1 + least[i - c = 5] ] gives least[6] = 1 + 1 = 2
     => c = 2, and minimum of[ least[6] = 12, 1 + least[i - c = 4] ] gives least[6] = 1 + 2 = 3
     => c = 5, and minimum of[ least[6] = 12, 1 + least[i - c = 1] ] gives least[6] = 1 + 1 = 2
     => => Result: least[6] = 2
Seventh iteration: 
i = 7,
     => c = 1 and minimum of[ least[7] = 12, 1 + least[i - c = 6] ] gives least[7] = 1 + 2 = 3
     => c = 2, and minimum of[ least[7] = 12, 1 + least[i - c = 5] ] gives least[7] = 1 + 1 = 2
     => c = 5, and minimum of[ least[7] = 12, 1 + least[i - c = 2] ] gives least[7] = 1 + 1 = 2
     => => Result: least[7] = 2
Eighth iteration: 
i = 8,
     => c = 1 and minimum of[ least[8] = 12, 1 + least[i - c = 7] ] gives least[8] = 1 + 2 = 3
     => c = 2, and minimum of[ least[8] = 12, 1 + least[i - c = 6] ] gives least[8] = 1 + 3 = 3
     => c = 5, and minimum of[ least[7] = 12, 1 + least[i - c = 3] ] gives least[7] = 1 + 1 = 3
     => => Result: least[8] = 3
Ninth iteration: 
i = 9,
     => c = 1 and minimum of[ least[9] = 12, 1 + least[i - c = 8] ] gives least[9] = 1 + 3 = 4
     => c = 2, and minimum of[ least[9] = 12, 1 + least[i - c = 7] ] gives least[9] = 1 + 2 = 3
     => c = 5, and minimum of[ least[7] = 12, 1 + least[i - c = 4] ] gives least[7] = 1 + 2 = 3
     => => Result: least[9] = 3
Tenth iteration: 
i = 10,
     => c = 1 and minimum of[ least[10] = 12, 1 + least[i - c = 9] ] gives least[10] = 1 + 3 = 4
     => c = 2, and minimum of[ least[10] = 12, 1 + least[i - c = 8] ] gives least[10] = 1 + 3 = 4
     => c = 5, and minimum of[ least[7] = 12, 1 + least[i - c = 5] ] gives least[7] = 1 + 1 = 2
     => => Result: least[10] = 2
Eleventh iteration: 
i = 11,
     => c = 1 and minimum of[ least[11] = 12, 1 + least[i - c = 10] ] gives least[11] = 1 + 2 = 3
     => c = 2, and minimum of[ least[11] = 12, 1 + least[i - c = 9] ] gives least[11] = 1 + 3 = 4
     => c = 5, and minimum of[ least[7] = 12, 1 + least[i - c = 6] ] gives least[7] = 1 + 2 = 3
     => => Result: least[11] = 3
So return 3.
Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)

Flaw: Tracking through least[i] gives different values.

## LeetCode 424. Longest Repeating Character Replacement
=> Algorithm: Sliding window
=> Note: Revise the algorithm from YouTube
=> Status: STAR
=> Tracing through two examples:
1. ABAABBA
{'A': 1}
1
{'A': 1, 'B': 1}
2
{'A': 2, 'B': 1}
3
{'A': 3, 'B': 1}
4
{'A': 3, 'B': 2}
5
{'A': 2, 'B': 3}
5
{'A': 3, 'B': 2}
5
5
2. ABAABAA
{'A': 1}
1
{'A': 1, 'B': 1}
2
{'A': 2, 'B': 1}
3
{'A': 3, 'B': 1}
4
{'A': 3, 'B': 2}
5
{'A': 4, 'B': 2}
6
{'A': 5, 'B': 2}
7
7
Time Complexity: O(n)
Space Complexity: O(Size of the hashmap)
## LeetCode 118. Pascal's Triangle
=> Algorithm:
=> Make sure all the edge cases has 1
=> Add the index values[i - 1][j - 1] and values[i - 1][j] for the rest
Example Tracing: 
=> Input = 5
=> [1]
=> [1,1]
=> [1,2,1]
=> [1,3,3,1]
=> [1,4,6,4,1]
Final Result: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
Time Complexity: O(n * S(n))
Space Complexity: O(n * S(n)) [check]
## LeetCode 27. Remove Element
`Bad Question`
=> Just use remove and calculate the new length 
and return the list
## LeetCode 125. Valid Palindrome
=> replace all punctuation with empty character
=> convert it to lowercase
=> reverse string == string => True else False
## LeetCode 136. Single Number
=> Method 1: Use Count on every element. Return who has one
=> Method 2: Use xor gate as xor gate of the same number results in 0. Whichever element occurs once will be left last (Efficient)
## LeetCode 14. Longest Common Prefix
=>Algorithm explanation: 
=>['flower', 'flow', 'flight']
=> Result = 'fl'
=> Iterate through the length of the 0th index 
=> Iterate through the list of strings
=> if len(string) == i or both strings not equal, return res
=> else add that character to result
=> return result
=> Status: Star[Flipped the loop to check everything together at once]
## LeetCode 389. Find the Difference
=> loop through every character in t
=> check if s.count(a) == t.count(a)
=> if not return a
## LeetCode 4. Median of Two Sorted Arrays
=> Append all numbers in one array
=> Sort the array
=> return mid th index + (mid + 1)th index/2 if even
=> else return mid index
=> Time complexity: O(n log n) [Sorting complexity takes importance over loop which is O(sizeof(nums2))]
=> Space Complexity: O(n)
## LeetCode 206. Reverse Linked List
=> [1] -> [2] -> [3] -> [None]
[prev] -> [curr] = loop
=> [None] <- [1] <- [2] <- [3]
=> Break Links and store it in a temporary variable
=> Time Complexity: O(n)
=> Space Complexity: O(1)
=> Trace: [None] <- [1]
=> [1] <- [2]
=> [2] <- [3]
=> Final: [3] -> [2] -> [1] -> [None]
## LeetCode 141. Linked List Cycle
=> return False if head is None
=> store every linked list object to an array
=> if object already in the array then return true
=> else return false
[Follow up: Can you solve it using O(1) (i.e. constant) memory?] **imp**
=> Floyd's Tortoise and Hare Detection Algorithm check.
## LeetCode 19. Remove Nth Node From End of List
=> Algorithm: Dummy first, Two pointer technique
=> Take left pointer and right pointer linked list objects
=> Iterate using right pointer
=> Increment left pointer only when count > n
=> We have the node before the node to be deleted
=> do lp.next = lp.next.next
=> Edge cases: [1] return None and removing first element: return head.next
=> Trace: 
[1,2,3,4,5] n = 2
To be deleted 4
Attach a dummy:
[0,1,2,3,4,5]
Iterate using the loop
1.   rp = 0
     lp = does not begin
2.   rp = 1
     lp = does not begin
3.   rp = 2
     lp = does not begin
4.   rp = 3
     lp = 1
5.   rp = 4
     lp = 2
6.   rp = 5
     lp = 3
[Check the tracing]
Time Complexity: O(n)
Space Complexity: O(n)
## LeetCode 143. Reorder List
Algorithm: 
=> Make two new lists
=> Reverse one list
=> Edit head such that even gets reversed indices
 and odd gets normal indices
=> Example: [1,2,3,4,5]
=> [1,5,2,4,3]
Two Lists:
Odd: [1,2,3]
Even: [4,5]
Time Complexity: O(n)
Space Complexity: O(n^2)
[Check]
Find a better solution for this
## LeetCode 149. Max Points on a Line
=> if length of points = 1 return 1, if length of points = 2 return 2
=> Use this formula = (y2 - y1) / (x2 - x1) to find if two points are collinear
=> Loop through all the points twice
=> Store all the slope of i indices in a hashmap:
=> Example: 0 -> [1.0,1.0,2.0]
=> Edge case: Slope might be equal to infinity
=> Use an arbitrarily big float number. Example: 1 -> [float_max,1.0,-2.5]
=> Once you have the slope array for all points. Find the max recurring slope and add 1 to it. return the max(added 1)
=> Example: [[1,1], [2,2], [3,3]] => All index have 1.0 has slopes, two times. Adding 1 gives the number of collinear points
=> Time Complexity: O(n^2)
=> Space Complexity: O(sizeof(hashmap) = sizeof(all possible slopes))
## LeetCode 204. Count Primes
Explanation pending
"Since all primes > 3 are of the form 6n ± 1, once we eliminate that n is:
not 2 or 3 (which are prime) and
not even (with n%2) and
not divisible by 3 (with n%3) then we can test every 6th n ± 1."
=> Status: Star
## LeetCode 73. Set Matrix Zeroes
=> Check the index of the x or y of zero in the original loop and store it in a loop
=> if index match, set that element to 0
## LeetCode 48. Rotate Image
Old Index:
[(0,0),(0,1),(0,2)]
[(1,0),(1,1),(1,2)]
[(2,0),(2,1),(2,2)]
Old Matrix:
[1,2,3]
[4,5,6]
[7,8,9]
New Index from old:
[(2,0),(1,0),(0,0)]
[(2,1),(1,1),(0,1)]
[(2,2),(1,2),(0,2)]
New Matrix:
[7,4,1]
[8,5,2]
[9,6,3]
Find a better solution with less space complexity and time complexity.
## LeetCode 202. Happy Number
=> if 1 return 1
=> else run an infinite loop
=> keep adding all the prev sum in an array
=> if thisNum in prev, return false [means it is a cycle]
=> if sum ever equals 1, just return true
=> Important: Check how to convert integers to lists using python
=> res = [int(n) for n in str(n)]
=> Time complexity: O(time to get 1 * every loop which adds all the numbers or N by context given below) or detect a cycle
=> Space Complexity: [Check], [O(N)] N is the size of array which has individual numbers
## LeetCode 26. Remove Duplicates from Sorted Array
=> check the count of every element
=> if the count is > 1 then
=> Remove the element until the count of that element becomes 1
## LeetCode 867. Transpose Matrix
=> Change the index from [i][j] to [j][i]
## 7. Reverse Integer
=> return 0 if it goes out of bounds
=> convert string and reverse, if negative remove '-' and then multiply by -1
=> return the converted string
=> Check algorithm without converting to strings
## Swap nodes in pairs:
=> Watch: https://youtu.be/o811TZLAWOo
=> Problem: Hard
=> Time Complexity: O(n)
=> Space Complexity: O(1)
## 57. Insert Interval
=> 1....4
=>    3....5
=> New interval = (1,5)
=> Condition: newInterval[1] >= interval[0] and newInterval[0] <= interval[1]
=> Edge cases: Add intervals if they dont overlap or the intervals are empty
=> Time complexity: O(n log n) My method, O(n) Youtube method
=> Space complexity: O(n), result array
## LeetCode 56. Merge Intervals
=> Sort the interval array using intervals.sort(key=lambda x: x[0])
=> Sort by the x value of the interval
=> Merge is similar to insert intervals
=> Keep popping stuff off the array when u get an interval that can be merged.
=> Time complexity: O(n logn)
=> Space Complexity: O(1)
## 54. Spiral Matrix
=> Explanation:
=> Youtube Video: https://youtu.be/BJnMZNwUk1M
=> Time Complexity: O(m * n)
=> Space Complexity: O(1)
## 79. Word Search
=> Recursion: https://youtu.be/pfiQ_PS1g8E
=> Time Complexity: O(n * m * (4 ^ n))
=> Space Complexity: O() [Confusion]
=> Status Star
## 1539. Kth Missing Positive Number
=> edge case of last number and then doing (k - count) + last element
## 41. First Missing Positive
=> Youtube: https://www.youtube.com/watch?v=8g78yfzMlao&t=748s

