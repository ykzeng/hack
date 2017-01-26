package com.yzeng.leetcode.easy;

public class Fibonacci {
	public static int getNumber(int n){
		if (n == 1) 
			return 0;
		else if (n == 2) 
			return 1;
		else if (n > 2) 
			return (getNumber(n - 1) + getNumber(n-2));
		else 
			return -1;
	}
	
	public static void main(String[] args){
		System.out.println(getNumber(13));
	}
}
