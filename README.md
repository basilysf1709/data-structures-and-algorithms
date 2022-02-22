Q. `LeetCode 238: Product of Array Except Self:`
Sol) Left and Right Products 
     Left: [1,2,3,4] => [1,1,2,6]
     Right: [1,2,3,4] => [24,12,4,1]
     Output: Left * Right => [24,12,8,6]
     Note: Left Index, loop is 1 to 3(1,2,3) and Right Index, loop is 2 to 0(2,1,0)
Q. `LeetCode 53: Maximum Sum Subarray:`
Sol) Kadane's Algorithm
     Eg: [-2,1,-3,4,-1,2,1,-5,4]
     => loopCounter from 0 to i - 1
     => set max and current to index 0, "-2" in this case
     => current = current + arr[loopCounter + 1]
     => if current < arr[loopCounter + 1], then current equals arr[loopCounter + 1]
     => if max < current, max = current
Q. `LeetCode 152: Maximum Product Subarray`
Sol) Kadane's Algorithm with currMin and currMax
     => initialize max as nums[0] for single array cases
     => nums[i] = 1, then currMin and currMax = 1
     => currMax = max of(n * currMax, n * currMin, n)
     => currMin = min of(n * currMax, n * currMin, n), (Careful: should be of this iteration, take a tmp at the start for currMax)
     => max = max of(currMax, max)
Q. `LeetCode 371-Sum of Two Integers without +/-`
Sol) Algorithm by example:
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
Q. `LeetCode `

