class Solution {
    public int maxArea(int[] height) {
        int area = 0;
        int curr = 0;
        int breadth = 0;
        
        for(int i = 0; i < height.length; i++) {
            
            breadth = 1;
            for(int j = i + 1; j < height.length; j++) {
                
                if (height[i] > height[j]) curr = height[j] * breadth; 
                else curr = height[i] * breadth;
                
                if(curr > area) area = curr;
                breadth++;
            }
        }
        
        return area;
    }
}