package com.yzeng.leetcode.medium;

public class Power {
//	public double myPow(double x, int n) {
//		double pow = 1.0;
//		boolean sign = true;
//		if (n <= 0) {
//			if (n == 0) {
//				return 1.0;
//			}
//			n = - n;
//			sign = false;
//		}
//		pow = recurPow(x, n);
//		return sign ? pow : (1.0 / pow);
//    }
//	
//	public double recurPow(double x, int n){
//		double tmp = 0.0;
//		if (n % 2 != 0) {
//			if (n == 1) 
//				return x;
//			else{
//				tmp = recurPow(x, ((n - 1) / 2));
//				return (x * tmp * tmp);
//			}
//		}
//		else{
//			tmp = recurPow(x, n / 2);
//			return (tmp * tmp);
//		}
//	}
	
	public double myPow(double x, int n) {
		double halfPow = 1.0, pow = 1.0;
		if (n == 0) {
			return 1.0;
		}
		if (n % 2 == 0) {
			halfPow = myPow(x, (n / 2));
			pow = halfPow * halfPow;
		}
		else {
			if (n > 0) {
				halfPow = myPow(x, (n / 2));
				pow = halfPow * halfPow * x;
			}
			else {
				halfPow = myPow(x, (n / 2));
				pow = halfPow * halfPow / x;
			}
		}
		return pow;
    }
	
	public static void main(String[] args){
		double x = 2.0;
		int n = -3;
		System.out.println(new Power().myPow(x, n));
	}
}
