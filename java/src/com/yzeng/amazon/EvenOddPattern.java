package com.yzeng.amazon;

public class EvenOddPattern {
	public static void printPattern(int num){
		int print = 0;
		if (num % 2 == 0) {
			print = 0;
			for (int j = 0; j < num; j++) {
				System.out.print(print + " ");
				print += 2;
			}
		}
		else{
			print = 1;
			for (int j = 0; j < num; j++) {
				System.out.print(print + " ");
				print += 2;
			}
		}
	}
	
	public static void main(String[] args){
		printPattern(7);
	}
}
