package com.yzeng.amazon;

public class SelectionSort {
	public static int[] selectSort(int[] arr){
		for (int i = 0; i < arr.length; i++) {
			int minIndex = i;
			for (int j = i; j < arr.length; j++) {
				if (arr[minIndex] > arr[j]) {
					minIndex = j;
				}
			}
			int temp = arr[i];
			arr[i] = arr[minIndex];
			arr[minIndex] = temp;
		}
		return arr;
	}
	
	public static void main(String[] args){
		int[] arr = {0, 5, 8, 1, 2, 4, 3, 5, 10};
		printArray(arr);
		selectSort(arr);
		printArray(arr);
	}
	
	public static void printArray(int[] arr){
		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
		}
		System.out.println();
	}
}
