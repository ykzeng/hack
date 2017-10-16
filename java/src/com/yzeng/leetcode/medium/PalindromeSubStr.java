package com.yzeng.leetcode.medium;

public class PalindromeSubStr {
	int count = 0;
    
    public int countSubstrings(String s) {
        for(int i = 0; i < s.length(); i ++){
            count += extend(s, i, i);
            count += extend(s, i, i+1);
        }
        return count;
    }
    
    public int extend(String s, int lo, int hi){
        int tmpCount = 0;
        while(lo >= 0 && hi < s.length() && s.charAt(lo) == s.charAt(hi)){
            tmpCount ++;
            lo --;
            hi ++;
        }
        return tmpCount;
    }
}
