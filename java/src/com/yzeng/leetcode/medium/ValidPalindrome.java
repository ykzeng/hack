package com.yzeng.leetcode.medium;

public class ValidPalindrome {
	public boolean isPalindrome(String s) {
        int head = 0, tail = s.length() - 1;
        while(head < tail){
            if(!Character.isLetterOrDigit(s.charAt(head))){      
                head ++;
                continue;
            }
            if(!Character.isLetterOrDigit(s.charAt(tail))){
                tail --;
                continue;
            }
            if(Character.toLowerCase(s.charAt(head)) == Character.toLowerCase(s.charAt(tail))){
                head ++;
                tail --;
            }
            else
                return false;
        }
        return true;
    }
	
	public static void main(String[] args){
		String input = "abca";//"A man, a plan, a canal: Panama";
		boolean isPalindrome = false;
		ValidPalindrome test = new ValidPalindrome();
		isPalindrome = test.isPalindrome(input);
		System.out.println(isPalindrome);
	}
}
