package com.yzeng.leetcode.medium;

import javax.sound.midi.Receiver;

public class JumpGame {
	//My top-down solution, will run overtime in last few test cases on LC
//	public boolean canJump(int[] nums) {
//		return canJump(nums, nums.length - 1);
//    }
//	
//	public boolean canJump(int[] nums, int pos){
//		if (pos == 0) {
//			return true;
//		}
//		for (int i = pos - 1; i >= 0; --i) {
//			if (canJump(nums, i) && pos - i <= nums[i]) {
//				return true;
//			}
//		}
//		return false;
//	}
	
	//Bottom-up fashion, idea from LC discussion
	public boolean canJump(int[] nums){
		int reach = 0;
		for (int i = 0; i <= reach && i < nums.length; i++) {
			int tmpMax = maxJump(nums, i);
			reach = tmpMax > reach ? tmpMax : reach;
			if (reach >= nums.length - 1) {
				return true;
			}
		}
		return false;
	}
	
	public int maxJump(int[] nums, int level){
		return nums[level] + level;
	}
	
	public static void main(String[] args){
		//int[] input = {2, 3, 1, 1, 4};
		int[] input = {0};
		//int[] input = {3, 2, 1, 0, 4};
		System.out.println(new JumpGame().canJump(input));
	}
}
