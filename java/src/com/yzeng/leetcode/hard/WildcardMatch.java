package com.yzeng.leetcode.hard;

public class WildcardMatch {
	public static void main(String[] args){
//		String s = "abcdefghijklmn", p = "ab**ef?*mn";
//		String s = "abbbb", p = "?*b**";
//		String s = "aaaa", p = "***a";
		String s = "", p = "*";
		System.out.println(new WildcardMatch().isMatch(s, p));
	}
	
	public boolean isMatch(String s, String p) {
		char[] strArray = s.toCharArray();
		char[] pattern = p.toCharArray();
		
		int pIndex = 0, sIndex = 0, pStar = -1, sStar = -1;
		while (sIndex < strArray.length) {
			if ((pIndex < pattern.length) && (strArray[sIndex] == pattern[pIndex] || pattern[pIndex] == '?')) {
				sIndex ++;
				pIndex ++;
			}
			else if ((pIndex < pattern.length) && (pattern[pIndex] == '*')) {
				pStar = ++ pIndex;
				sStar = sIndex;
			}
			else {
				if (pStar == -1) {
					return false;
				}
				else{
					pIndex = pStar;
					sIndex = ++sStar;
				}
			}
		}
			
		while (pIndex < pattern.length && pattern[pIndex] == '*') {
				pIndex ++;
			}
		
		if (pIndex == pattern.length) {
			return true;
		}
		else
			return false;
    }
}
