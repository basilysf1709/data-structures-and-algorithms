class Solution {
    public int maxArea(int[] height) {
        
        int area = 0;
        
        int start = 0;
        int finish = height.length - 1;
        
        while(start < finish) {
            if(height[start] < height[finish]) {
                area = Math.max(area, (finish - start) * height[start]);
                start++;
            }
            else {
                area = Math.max(area, (finish - start) * height[finish]);
                finish--;
            }
        }
        
        return area;
    }
}