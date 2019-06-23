package com.yzeng.cc150;

import java.util.Arrays;
import java.util.HashMap;

public class RepetitiveStr {
//	public boolean detectStrRep(String string){
//		HashMap<String, Boolean> charMap = new HashMap<>();
//		for (int i = 0; i < string.length(); i++) {
//			if (charMap.containsKey(string.substring(i, i))) {
//				return false;
//			}
//		}
//		return true;
//	}
	// suppose we are talking about 256 ascii
	public boolean detectStrRep(String string){
		// every int contains 32 bits
		// in total 32*8=256 bits
		int[] exist = new int[8];
		Arrays.fill(exist, 0);
		for (int i = 0; i < string.length(); i++) {
			int cur = (int)string.charAt(i), 
				index1 = i/32, index2 = i%32, 
				temp = (int)Math.pow(2, index2);
			if ((exist[index1] & temp) == temp) {
				return false;
			}
		}
		return true;
	}
}
