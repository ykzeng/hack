package com.yzeng.hack.easy;

import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class NonDivisibleSubset {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    	Scanner in = new Scanner(System.in);
        int length = in.nextInt();
        int number = in.nextInt();
        HashMap<Integer, ArrayList<Integer>> hashMap = new HashMap<Integer, ArrayList<Integer>>();
        for (int i = 0; i < number; i++) {
			hashMap.put(i, new ArrayList<Integer>());
		}
        int next = 0;
        for (int i = 0; i < length; i++) {
			next = in.nextInt();
			ArrayList<Integer> hashEntry = hashMap.get((next % number));
			hashEntry.add(next);
		}
        in.close();
        int count = 0;
        if (hashMap.get(0).size() != 0) {
			count ++;
		}
        int temp_len;
        if (number % 2 == 1) {
			temp_len = number / 2 + 1;
		}
        else{
        	temp_len = number / 2;
        	count ++;
        }
        //count = (number % 2 == 1) ? count : (count++);
        for (int i = 1; i < temp_len; i++) {
        	int smallSize = hashMap.get(i).size();
        	int largeSize = hashMap.get(number - i).size();
			count += smallSize > largeSize ? smallSize : largeSize;
		}
        System.out.println(count);
        
    }
}