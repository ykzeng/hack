package com.yzeng.leetcode.medium;

import java.util.HashMap;
import java.util.Scanner;

public class LongestSubstringNoRep {
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		String str = scanner.nextLine();
		System.out.println(new LongestSubstringNoRep().lengthOfLongestSubstring(str));
	}
	
	public int lengthOfLongestSubstring(String s) {
		if (s.equals("")) {
			return 0;
		}
        String longestSs = s.substring(0, 1);
        for (int i = 0; i < s.length(); i++) {
            String tmpSs = "";
			for (int j = i; j < s.length(); j++) {
				String currentChar = s.substring(j, j + 1);
				if (!tmpSs.contains(currentChar)) {
					tmpSs += currentChar;
				}
				else {
					break;
				}
			}
			if (tmpSs.length() > longestSs.length()) {
				longestSs = tmpSs;
			}
		}
        return longestSs.length();
		
		//Editorial
//		if (s.length()==0) return 0;
//        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
//        int max=0;
//        for (int i=0, j=0; i<s.length(); ++i){
//            if (map.containsKey(s.charAt(i))){
//                j = Math.max(j,map.get(s.charAt(i))+1);
//            }
//            map.put(s.charAt(i),i);
//            max = Math.max(max,i-j+1);
//        }
//        return max;
    }
}
