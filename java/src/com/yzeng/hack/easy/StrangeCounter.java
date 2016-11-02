package com.yzeng.hack.easy;

import java.util.Scanner;

public class StrangeCounter {
	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long t = in.nextLong();
        
        long cycle = 3, curretT = 0;
        while (true) {
			for (long i = cycle; i > 0; i--) {
				curretT ++;
				if (curretT == t) {
					System.out.println(i);
					return;
				}
			}
			cycle = cycle * 2;
		}
    }
}
