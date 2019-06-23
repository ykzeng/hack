package com.yzeng.leetcode.easy;

public class Atoi {
//	public int myAtoi(String str) {
//        if (str == null || str.equals("")) {
//			return 0;
//		}
//        char[] strChar = str.toCharArray();
//        int result = 0, start = 0;
//        for (int i = 0; i < strChar.length; i++) {
//			if (strChar[i] == ' ') {
//				start ++;
//			}
//		}
//        int minus = 1;
//        switch (strChar[start]) {
//			case '-':
//				minus = -1;
//			case '+':
//				start ++;
//				break;
//		}
//        
//        for (int i = start; i <= strChar.length - 1 ; i++) {
//			char digit = strChar[i];
//			if (digit >= 48 && digit <= 57) {
//				result += (digit - 48) * Math.pow(10, strChar.length - i - 1);
//				if (minus == 1 && result >= Integer.MAX_VALUE) {
//					return Integer.MAX_VALUE;
//				}
//				else if (minus == -1 && (result * minus) <= Integer.MIN_VALUE) {
//					return Integer.MIN_VALUE;
//				}
//			}
//			else{
//				result /= Math.pow(10, strChar.length - i);
//				return minus * result;
//			}
//		}
//        return minus * result;
//    }
	public int myAtoi(String str){
		// 1. white space before
		// 2. sign
		// 3. overflow
		// 4. letter in middle of numbers
		if (str.isEmpty()) {
			return 0;
		}
		char[] strChar = str.toCharArray();
		int start = 0, sign = 1, sum = 0;
		while (strChar[start] == ' ') {
			start ++;
		}
		if (strChar[start] == '+' || strChar[start] == '-') {
			sign = strChar[start] == '-' ? -1 : 1;
			start ++;
		}
		for (int i = start; i < strChar.length; i++) {
			if (Character.isDigit(strChar[i])) {
				int digit = strChar[i] - '0';
				if (Integer.MAX_VALUE / 10 < sum || (Integer.MAX_VALUE / 10 == sum && digit >= 8)) {
					return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
				}
				sum = sum * 10 + digit;
			}
			else 
				break;
		}
		return sum * sign;
	}
	
	public static void main(String[] args){
		String string = "   -012a48";
		//String string = "   +0 123";
		//String string = "-2147483648";
		System.out.println(new Atoi().myAtoi(string));
	}
}
