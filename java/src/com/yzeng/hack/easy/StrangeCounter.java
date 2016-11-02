package com.yzeng.hack.easy;

import java.util.Scanner;

public class StrangeCounter {
	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long t = in.nextLong();
        if (t <= 3) {
			System.out.println(3 - t + 1);
			return;
		}
        
        long currentMax = 3, lastMax = 0, currentCycle = 0;
        int  i = 2;
        for (i = 2; t > currentMax; i++) {
        	lastMax = currentMax;
			currentMax = 3 * (long)(1 - Math.pow((double)2, (double)i)) / (1 - 2);
			currentCycle = (3 * ((long)Math.pow(2, (i-1))));
		}
        System.out.println((currentCycle - (t - lastMax) + 1));
    }
}
