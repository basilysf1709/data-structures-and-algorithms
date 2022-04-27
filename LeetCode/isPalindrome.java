package LeetCode;
public class isPalindrome{
    // my attempt
    // public static boolean isPalindrome(int x) {
    //     int sum = 0;
    //     int y = 0;
    //     int i = 1;
    //     int k = x;
    //     while(x != 0){
    //         y = x;
    //         y = y % 10;
    //         sum += y*i;
    //         x = x / 10;
    //         i *= 10;
    //     }
    //     if(sum == k && k >= 0) return true;
    //     return false;
    // }
     // Special cases:
        // As discussed above, when x < 0, x is not a palindrome.
        // Also if the last digit of the number is 0, in order to be a palindrome,
        // the first digit of the number also needs to be 0.
        // Only 0 satisfy this property.
        // When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        // For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        // since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.

    public static boolean isPalindrome(int x) {
        if(x < 0 || (x % 10 == 0 && x != 0)) return false;
        int revNum = 0;
        while(x > revNum){
            revNum = revNum * 10 + x % 10;
            x /= 10;
        }
        return x == revNum || x == revNum/10;
    }
    // odd numbers middle digit doesn't matter. we are basically checking 12321, if 12 = 21(reversed)
    public static void main(String[] args){
        System.out.println(isPalindrome(12321));
    }
}
