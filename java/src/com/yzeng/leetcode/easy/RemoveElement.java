package com.yzeng.leetcode.easy;

public class RemoveElement {
	public static int removeElement(int[] nums, int val) {
		int count = 0, lastIndex = 0, tmpIndex = 0;
		int length = nums.length;
        for (int i = 0; i < length; i++) {
			if (nums[i] == val) {
				lastIndex = length - count;
				tmpIndex = lastIndex - 1;
				if (i == lastIndex) {
					return lastIndex;
				}
				nums[i] = nums[tmpIndex];
				nums[tmpIndex] = val;
				count ++;
				i--;
			}
		}
        return (lastIndex);
    }
	
	public static void main(String[] args){
		int[] test = {3, 2, 2, 3};
		removeElement(test, 3);
		for (int i = 0; i < test.length; i++) {
			System.out.println(test[i] + " ");
		}
	}
}
