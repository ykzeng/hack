package com.yzeng.leetcode.easy;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.function.IntPredicate;

public class TwoSum {
	// O(n), linear hashmap solution
//	public static int[] twoSum(int[] nums, int target) {
//		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
//		for (int i = 0; i < nums.length; map.put(nums[i], i), i++) {
//			if (map.containsKey(target - nums[i])) {
//				return (new int[]{map.get(target - nums[i]), i});
//			}
//		}
//		return null;
//    }
	
	// nlogn, two pointer solution
	public static int[] twoSum(int[] nums, int target) {
		int[] index = new int[nums.length];
		for (int i = 0; i < index.length; i++) {
			index[i] = i;
		}
		int[] sorted = qSortEntry(nums, index);
		int low = 0, high = nums.length - 1;
		while (low < high) {
			int sum = sorted[low] + sorted[high];
			if (sum == target) {
				return new int[]{index[low], index[high]};
			}
			else if (sum < target) {
				low ++;
			}
			else {
				high --;
			}
		}
		return null;
    }
	
	public static int indexOf(int[] nums, int target){
		for (int i = 0; i < nums.length; i++) {
			if (nums[i] == target) {
				return i;
			}
		}
		return -1;
	}
	
	public static int[] qSortEntry(int[] nums, int[] index){
		int[] copy = nums.clone();
		qSort(index, copy, 0, copy.length - 1);
		return copy;
	}
	
	public static void qSort(int index[], int anData[], int nLeft, int nRight)
    {
    	int nPivot = anData[nLeft + (nRight - nLeft) / 2];
    	int i = nLeft;
    	int j = nRight;
    	while (i <= j)
    	{
    		while (anData[i] < nPivot) ++i;

    		while (anData[j] > nPivot) --j;

    		if (i <= j)
    		{
    			int nTemp = anData[i];
    			anData[i] = anData[j];
    			anData[j] = nTemp;
    			int iTemp = index[i];
    			index[i] = index[j];
    			index[j] = iTemp;
    			++i;
    			--j;
    		}
    	}

    	if (nLeft < j) qSort(index, anData, nLeft, j);

    	if (nRight > i) qSort(index, anData, i, nRight);
    }
	
	public static void swap(int[] nums, int index1, int index2){
		int temp = nums[index1];
		nums[index1] = nums[index2];
		nums[index2] = temp;
	}
	
	public static void main(String[] args){
		int[] nums = {3, 2, 4};
		twoSum(nums, 6);
	}
}
