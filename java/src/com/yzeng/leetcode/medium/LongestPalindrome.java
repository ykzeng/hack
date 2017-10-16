package com.yzeng.leetcode.medium;

public class LongestPalindrome {

    int start = 0, maxLen = 1;
	
	public String longestPalindrome(String s) {
        for (int i = 0; i < s.length(); i ++){
            extend(s, i, i);
            extend(s, i, (i+1));
        }
        return s.substring(start, (start + maxLen));
    }
    
    public void extend(String s, int lo, int hi){
    	int newLen = 1;
        while(lo >= 0 && hi < s.length() && s.charAt(lo) == s.charAt(hi)){
        	newLen = hi - lo + 1;
            lo --;
            hi ++;
        }
        if (newLen > maxLen){
            maxLen = newLen;
            start = lo + 1;
        }
    }
    
    public static void main(String[] args){
    	String input = "aaac";//"abba";
    	LongestPalindrome palindrome = new LongestPalindrome();
    	String longest = palindrome.longestPalindrome(input);
    	System.out.println(longest);
    }
}
