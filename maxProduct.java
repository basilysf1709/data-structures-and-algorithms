class Solution {
    
    public int maxProduct(int[] nums) {
        int max = nums[0];
        int currMin = 1;
        int currMax = 1;
        
        for(int i = 0; i < nums.length; i++){
            if(i == 0){
                currMin = 1;
                currMax = 1;
            }
            int tmp = currMax * nums[i];
            currMax = Math.max(Math.max(nums[i] * currMax, nums[i] * currMin), nums[i]);
            currMin = Math.min(Math.min(tmp, nums[i] * currMin), nums[i]);
            max = Math.max(max, currMax);
        }
        
        return max;
    }
}