package com.yzeng.leetcode.easy;

public class ReverseInteger {
//	public static int reverse(int x){
//		String input = String.valueOf(x), output = "";
//		for (int j = input.length() - 1; j >= 0; j--) {
//			output += input.substring(j, j + 1);
//		}
//		if (x < 0) {
//			output = "-" + output.substring(0, output.length() - 1);
//		}
//		long result = Long.valueOf(output);
//		if(result > Integer.MAX_VALUE || result < Integer.MIN_VALUE)
//			return 0;
//		else
//			return (int)result;
//	}
	
	public static int reverse(int x){
		int input = x;
		long result = 0;
		while(x != 0){
			result = (result * 10 + x % 10);
			x = x / 10;
		}
		result = input < 0 ? -result : result;
		if (result > Integer.MAX_VALUE || result < Integer.MIN_VALUE) {
			return 0;
		}
		else
			return (int)result;
	}
	
	public static void main(String[] args){
		int input = -534236469;
		System.out.println(reverse(input));
	}
}
