package LeetCode;

class Solution {
    public int maxSubArray(int[] nums) {
        int curr = nums[0];
        int max = nums[0];
        for(int i = 1; i < nums.length; i++) {
            curr += nums[i];
            if(curr < nums[i]) curr = nums[i];
            if(curr > max) max = curr;
        }
        return max;
    }
}

