package LeetCode;
import java.util.Arrays;

class Solution {
    public boolean isAnagram(String s, String t) {
        char arr[] = s.toCharArray();
        char arr1[] = t.toCharArray();
        int count = 0;
        
        Arrays.sort(arr);
        Arrays.sort(arr1);
        
        if(s.length() != t.length()) return false;
        
        for(int i = 0; i < arr.length; i++) {
            if(arr[i] == arr1[i]) count++;
        }
        
        if(count == arr.length) return true;
        
        return false;
    }
}