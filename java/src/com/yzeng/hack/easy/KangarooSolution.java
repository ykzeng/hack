package com.yzeng.hack.easy;

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class KangarooSolution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int x1 = in.nextInt();
        int v1 = in.nextInt();
        int x2 = in.nextInt();
        int v2 = in.nextInt();
        in.close();
        
        int s1, s2;
        int second = 1;
        if (x1 == x2) {
			System.out.println("YES");
			return;
		}
        while(true){
        	s1 = x1+v1*second;
        	s2 = x2+v2*second;
        	if (s1 == s2) {
				System.out.println("YES");
				return;
			}
        	if (Math.abs(s1-s2) >= Math.abs(x1 - x2) ) {
				System.out.println("NO");
				return;
			}
        	second ++;
        }
    }
}
