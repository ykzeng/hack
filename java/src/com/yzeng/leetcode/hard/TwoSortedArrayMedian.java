package com.yzeng.leetcode.hard;

import java.util.Scanner;

public class TwoSortedArrayMedian {
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		
		String line = scanner.nextLine();
		String[] line1Array = line.replaceAll("\\[", "").replaceAll("\\]", "").replaceAll(" ", "").split(",");
		line = scanner.nextLine();
		String[] line2Array = line.replaceAll("\\[", "").replaceAll("\\]", "").replaceAll(" ", "").split(",");
		int[] nums1 = new int[line1Array.length], nums2 = new int[line2Array.length];
		for (int i = 0; i < line1Array.length; i++) {
			nums1[i] = Integer.valueOf(line1Array[i]);
		}
		for (int i = 0; i < line2Array.length; i++) {
			nums2[i] = Integer.valueOf(line2Array[i]);
		}
		double median = findMedianSortedArrays(nums1, nums2);
		System.out.println(median);
	}
	
	public static double getSortedArrayMedian(int[] nums){
		int len = nums.length, m2Pos = len / 2;
		if (len % 2 == 0) {
			return ((double)(nums[m2Pos - 1] + nums[m2Pos]) / 2);
		}
		else
			return nums[m2Pos];
	}
	
	public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        //
		if (nums1.length == 0 && nums2.length == 0) {
			return 0.0;
		}
		else if (nums1.length == 0) {
			return getSortedArrayMedian(nums2);
		}
		else if (nums2.length == 0) {
			return getSortedArrayMedian(nums1);
		}
		int lenSum = nums1.length + nums2.length;
		int median1Pos = -1, median2Pos = -1;
		if (lenSum % 2 == 0) {
			median1Pos = lenSum / 2 - 1;
			median2Pos = median1Pos + 1;
		}
		else
			median2Pos = lenSum / 2;
		int last = 0, current = 0, lastArray = 1;
		int i = 0, j = 0, total = 0, median1 = 0;
		boolean hasMedian1 = false;
		// while iterating two arrays
		for (; i < nums1.length && j < nums2.length;) {
			if (nums1[i] < nums2[j]) {
				current = nums1[i];
				lastArray = 1;
				i ++;
			}
			else{
				current = nums2[j];
				lastArray = 2;
				j ++;
			}
			if (total == median2Pos){
				return median1Pos == -1 ? current : ((double)(current + last) / 2);
			}
			else if (total == median1Pos) {
				median1 = current;
				hasMedian1 = true;
			}
			last = current;
			total ++;
		}
		// one of the array ran out
		int median2 = 0, distance = median2Pos - total;
		if (lastArray == 1) {
			median2 = nums2[j + distance];
			if (median1Pos != -1 && !hasMedian1) {
				median1 = nums2[j + distance - 1];
			}
		}
		else{
			median2 = nums1[i + distance];
			if (median1Pos != -1 && !hasMedian1) {
				median1 = nums1[i + distance - 1];
			}
		}
		return median1Pos == -1 ? median2 : ((double)(median1 + median2) / 2);
    }
}
