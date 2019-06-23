package com.yzeng.leetcode.medium;

//TODO should use dp to solve this problem
public class SubStrInWrapAroundStr {
	public int findSubstringInWraproundString(String p) {
        char[] cArray = p.toCharArray();
        int maxCount = 1, tmpCount = 1;
        for (int i = 0; i < (cArray.length - 1); i ++) {
        	// TODO how to increment i, 
			// a to z
        	if (cArray[i] >= 97 && cArray[i] <= 122) {
				if (cArray[i + 1] - cArray[i] == 1){
					tmpCount ++;
					continue;
        		}
				else if (cArray[i + 1] - cArray[i] == -25) {
					if (cArray[i] == 'z') {
						tmpCount ++;
						continue;
					}
				}
				maxCount = tmpCount > maxCount ? tmpCount : maxCount;
				tmpCount = 1;
			}
        	else
        		return -1;
		}
        maxCount = tmpCount > maxCount ? tmpCount : maxCount;
        int subCount = 0;
        for (int i = 1; i < maxCount; i++) {
			subCount += i;
		}
        subCount += cArray.length;
        return subCount;
    }
	
	public static void main(String[] args){
		SubStrInWrapAroundStr obj = new SubStrInWrapAroundStr();
		System.out.println(obj.findSubstringInWraproundString("zab"));
	}
}
