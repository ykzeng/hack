package com.yzeng.hack.easy;

import java.util.Scanner;

public class StrangeCounter {
	public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        
        int cycle = 3, curretT = 0, currentValue = 3;
        while (true) {
        	currentValue = cycle + 1;
			for (int i = 0; i < cycle; i++) {
				curretT ++;
				currentValue --;
				if (curretT == t) {
					System.out.println(currentValue);
					return;
				}
			}
			cycle = cycle * 2;
		}
        
    }
}
