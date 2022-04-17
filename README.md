# LeetCode Questions & Algorithms

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

# LeetCode 424. Longest Repeating Character Replacement
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
# LeetCode 118. Pascal's Triangle
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
# LeetCode 27. Remove Element
`Bad Question`
=> Just use remove and calculate the new length 
and return the list
# LeetCode 125. Valid Palindrome
=> replace all punctuation with empty character
=> convert it to lowercase
=> reverse string == string => True else False
# LeetCode 136. Single Number
=> Method 1: Use Count on every element. Return who has one
=> Method 2: Use xor gate as xor gate of the same number results in 0. Whichever element occurs once will be left last (Efficient)
# LeetCode 14. Longest Common Prefix
=>Algorithm explanation: 
=>['flower', 'flow', 'flight']
=> Result = 'fl'
=> Iterate through the length of the 0th index 
=> Iterate through the list of strings
=> if len(string) == i or both strings not equal, return res
=> else add that character to result
=> return result
=> Status: Star[Flipped the loop to check everything together at once]
# LeetCode 389. Find the Difference
=> loop through every character in t
=> check if s.count(a) == t.count(a)
=> if not return a
# LeetCode 4. Median of Two Sorted Arrays
=> Append all numbers in one array
=> Sort the array
=> return mid th index + (mid + 1)th index/2 if even
=> else return mid index
=> Time complexity: O(n log n) [Sorting complexity takes importance over loop which is O(sizeof(nums2))]
=> Space Complexity: O(n)
# LeetCode 206. Reverse Linked List
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
# LeetCode 141. Linked List Cycle
=> return False if head is None
=> store every linked list object to an array
=> if object already in the array then return true
=> else return false
[Follow up: Can you solve it using O(1) (i.e. constant) memory?] **imp**
=> Floyd's Tortoise and Hare Detection Algorithm check.