package com.yzeng.algorithms;

import java.util.Random;

public class Sort {
	public static int[] randomArray(int minLen, int maxLen, int bound){
		Random random = new Random(System.currentTimeMillis());
		int length = random.nextInt(maxLen - minLen) + 1 + minLen;
		int[] array = new int[length];
		for (int i = 0; i < length; i++) {
			array[i] = random.nextInt(bound);
		}
		return array;
	}
	
	public static void printArray(int[] array){
		System.out.print("{");
		for (int i = 0; i < array.length - 1; i++) {
			System.out.print(array[i] + ", ");
		}
		System.out.print(array[array.length - 1] + "}");
		System.out.println();
	}
	
	public static void main(String[] args){
		// random array generation
		int[] test1 = randomArray(5000, 5001, 100), test2 = test1.clone();
		System.out.println("Array before sorting: ");
		printArray(test1);
		
		// improved insertion sort
		long start = System.currentTimeMillis();
		int[] sorted = insertionSort(test1);
		System.out.println("Runtime: " + (System.currentTimeMillis() - start) + "ms");
		
		System.out.println("Array after sorting: ");
		printArray(sorted);
		
		// my insertion sort
		//System.out.println("Array before sorting: ");
		//printArray(test2);

		start = System.currentTimeMillis();
		sorted = myInsertSort(test2);
		System.out.println("Runtime: " + (System.currentTimeMillis() - start) + "ms");
		
		System.out.println("Array after sorting: ");
		printArray(sorted);
	}
	
	public static int[] insertionSort(int[] array){
		for (int i = 1; i < array.length; i++) {
			int swap = array[i], j = i;
			while (j > 0 && array[j - 1] < swap) {
				array[j] = array[j - 1];
				j --;
			}
			array[j] = swap;
		}
		return array;
	}
	
	public static int[] myInsertSort(int[] array){
		for (int i = 1; i < array.length; i++) {
			for (int j = 0; j < i; j++) {
				if (array[j] < array[i]) {
					int swap = array[i];
					array[i] = array[j];
					array[j] = swap;
				}
			}
		}
		return array;
	}
}
