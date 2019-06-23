package com.yzeng.twosigma; 


public class LongestIncrSubSeq {
	
	public static void main(String[] args){
		long start = 0, end = 0;
		
		int [] input1 = {3, 10, 2, 1, 20, 30, 9, 31, 18, 20, 99, 100};
		System.out.println("Standard function: ");
		start = System.currentTimeMillis();
		System.out.println(lengthOfLIS(input1));
		end = System.currentTimeMillis();
		System.out.println("Running time: " + (end - start) + " ms");
		
		System.out.println("\nMy solution: ");
		start = System.currentTimeMillis();
		System.out.println(liss(input1));
		end = System.currentTimeMillis();
		System.out.println("Running time: " + (end - start) + " ms");
		
		int[] input2 = {50, 3, 10, 7, 40, 80};
		System.out.println("Standard function: ");
		System.out.println(lengthOfLIS(input2));
		System.out.println("My solution: ");
		System.out.println(liss(input2));

		int [] input3 = {4, 10, 4, 3, 8, 9};
		System.out.println("Standard function: ");
		System.out.println(lengthOfLIS(input3));
		System.out.println("My solution: ");
		System.out.println(liss(input3));
	}
	
//	public static int lengthOfLIS(int[] nums) {
//		if (nums.length == 0) {
//        	return 0;
//		}
//		// record the length of longest sub sequence at each index
//		int[] maxLen = new int[nums.length];
//		maxLen[0] = 1;
//		for(int i = 1; i < maxLen.length; i ++){
//			int maxCur = 0;
//			for (int j = 0; j < i; j++) {
//				int temp = maxLen[j];
//				if (nums[j] < nums[i]) {
//					temp ++;
//				}
//				maxCur = maxCur > temp ? maxCur : temp;
//			}
//			maxLen[i] = maxCur;
//		}
//		return maxLen[nums.length - 1];
//    }
	
	public static int liss(int[] nums){
		int[] maxLen = new int[nums.length];
		maxLen[0] = 1;
		
		int result = 0;
		for (int i = 1; i < nums.length; i++) {
			int maxCur = 0;
			for (int j = 0; j < i; j++) {
				if (nums[j] < nums[i]) {
					maxCur = maxCur > maxLen[j] ? maxCur : maxLen[j];
				}
			}
			maxLen[i] = ++maxCur;
			result = result > maxLen[i] ? result : maxLen[i];
		}
		return result;
	}
	
	
	public static int lengthOfLIS(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int[] dp = new int[nums.length];
        dp[0] = 1;
        int maxans = 1;
        for (int i = 1; i < dp.length; i++) {
            int maxval = 0;
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    maxval = Math.max(maxval, dp[j]);
                }
            }
            dp[i] = maxval + 1;
            maxans = Math.max(maxans, dp[i]);
        }
        return maxans;
    }
}
