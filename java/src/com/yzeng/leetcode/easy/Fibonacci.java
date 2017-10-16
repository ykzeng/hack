package com.yzeng.leetcode.easy;

public class Fibonacci {
	// naive recursive solution
	public static long fib1(int n){
		if(n <= 2)
			return 1;
		else 
			return fib1(n - 1) + fib1(n - 2);
	}
	// recursive solution with memoization
	public static long fib2(int n){
		long[] memo = new long[n];
		memo[0] = 1;
		memo[1] = 1;
		return fibMemo((n - 1), memo);
	}
	
	public static long fibMemo(int n, long[] memo){
		if (memo[n] == 0) {
			memo[n] = fibMemo(n - 1, memo) + fibMemo(n - 2, memo);
		}
		return memo[n];
	}
	
	// bottom-up recursive solution
	public static long fib3(int n){
		long[] memo = new long[n];
		memo[0] = 1;
		memo[1] = 1;
		for (int i = 2; i < n; i++) {
			memo[i] = memo[i - 1] + memo[i - 2];
		}
		return memo[n - 1];
	}
	
	public static void main(String[] args){
		int test = 80;
		long start = System.currentTimeMillis(), end = 0;
		System.out.println(fib2(test));
		end = System.currentTimeMillis();
		System.out.println("with Memoization Running Time: " + (end - start) + " ms");
		
		start = System.currentTimeMillis();
		System.out.println(fib3(test));
		end = System.currentTimeMillis();
		System.out.println("Loop with Memoization Running Time: " + (end - start) + " ms");
		
		start = System.currentTimeMillis();
		System.out.println(fib1(test));
		end = System.currentTimeMillis();
		System.out.println("Pure Recursive Running Time: " + (end - start) + " ms");
	}
}
