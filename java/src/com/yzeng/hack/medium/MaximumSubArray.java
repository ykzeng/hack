package com.yzeng.hack.medium;

import java.io.InputStream;
import java.util.Scanner;

import javax.xml.transform.Templates;

public class MaximumSubArray {
	public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int caseCount = Integer.valueOf(in.nextLine());
		String [] input = new String[caseCount * 2];
		for (int i = 0; i < input.length; i++) {
			input[i] = in.nextLine();
		}
		in.close();
		for (int i = 0; i < input.length; i += 2) {
			int length = Integer.valueOf(input[i]);
			String [] strs = input[i+1].split(" ");
			int [] nums = new int[length];
			for (int j = 0; j < strs.length; j++) {
				nums[j] = Integer.valueOf(strs[j]);
			}
			maxSubArray(nums);
		}
	}
	
	//contiguous
	public static void maxSubArray(int[] nums) {
		int max = nums[0];
		int nonMax = max > 0 ? max : 0, conMax = 0;
		for (int i = 1; i < nums.length; i++) {
			if(nums[i] > max)
				max = nums[i];
			if (nums[i] > 0) {
				nonMax += nums[i];
			}
		}
		if (max <= 0) {
			conMax = nonMax = max;
			System.out.println(max + " " + max);
			return;
		}
		
		int maxSum = 0;
		int sum = 0;
		for (int i = 0; i < nums.length; i++) {
			if (nums[i] < 0) {
				sum = (sum + nums[i]) > 0 ? (sum + nums[i]) : 0;
			}
			else{
				sum += nums[i];
				maxSum = sum > maxSum ? sum : maxSum;
			}
		}
		System.out.println(maxSum + " " + nonMax);
		return;
    }
}
