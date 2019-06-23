package com.yzeng.algorithms;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Random;

public class MStormBFS {
	
	// assignment
	
	public MStormBFS(){
		
	}
	
	public static int[] randArray(int indexBound, int valBound){
		Random random = new Random(System.currentTimeMillis());
		int length = random.nextInt(indexBound - 1) + 2;
		int[] array = new int[length];
		for (int i = 0; i < array.length; i++) {
			array[i] = random.nextInt(valBound - 1) + 2;
		}
		return array;
	}
	
	// returns true if all component tasks are allocated, returns false if no
	public static boolean bfsAssign(int [] exptExecutorsOfDevice, String[] compNames, HashMap<String, Integer> compName2TaskNum){
		int[] exeOnDevice = exptExecutorsOfDevice.clone(), taskPerLv;
		// task number for each component
		// get the task count of multi level components respectively
		taskPerLv = new int[compNames.length];
		for (int i = 0; i < compNames.length; i++) {
			taskPerLv[i] = compName2TaskNum.get(compNames[i]);
		}
		// TODO randomly generate tasks and components here
		//int[] exeOnDevice = randArray(6, 6), taskPerLv = randArray(6, 5);
		//passed
		//int[] exeOnDevice = {6, 5, 4, 3, 3}, taskPerLv = {4, 4, 4, 3, 2};
		//passed
		//int[] exeOnDevice = {2, 5, 4, 6}, taskPerLv = {5, 4, 2, 2};
		//passed
		//int[] exeOnDevice = {5, 2, 4, 3, 4}, taskPerLv = {3, 4, 3, 4, 2};
		// the device count and component count
		int devCount = exeOnDevice.length, compCount = taskPerLv.length;
		// init the assignment matrix
		int[][] assign = new int[devCount][compCount];
		for (int i = 0; i < assign.length; i++) {
			Arrays.fill(assign[i], 0);
		}
		
		int exeNum, rootLv = 0;
		for (int j = 0; j < devCount; j++) {
			// remaining executor number of current assigning device, start at dev 0
			exeNum = exeOnDevice[j];
			for (int i = 0; i < taskPerLv.length; i++) {
				if (taskPerLv[i] > 0) {
					rootLv = i;
					break;
				}
			}
			int ret = bfs(rootLv, exeNum, taskPerLv, assign[j]);
			if (ret != 0) {
				return true;
			}
		}
		for (int i = 0; i < taskPerLv.length; i++) {
			if (taskPerLv[i] != 0) {
				return false;
			}
		}
		return true;
	}
	
	public static int bfs(int rootLv, int exeNum, int[] taskPerLv, int[] assignment){
		if (rootLv >= taskPerLv.length) {
			return exeNum;
		}
		taskPerLv[rootLv]--;
		assignment[rootLv]++;
		exeNum--;
		for (int i = rootLv + 1; i <= taskPerLv.length; i++) {
			// theorem: only when we are one level from root component we can get this condition
			if (i == taskPerLv.length || taskPerLv[i] == 0) {
				// last level task more than executor number
				// allocate all executors on device for last level tasks
				if (taskPerLv[i - 1] >= exeNum) {
					assignment[i - 1] += exeNum;
					taskPerLv[i - 1] -= exeNum;
					exeNum = 0;
					return exeNum;
				}
				// last level tasks less than device executor
				// allocate all tasks to the device and continue to the next level
				else{
					assignment[i - 1] += taskPerLv[i - 1];
					exeNum -= taskPerLv[i - 1];
					taskPerLv[i - 1] = 0;
					
					return bfs(i + 1, exeNum, taskPerLv, assignment);
				}
			}
			else if (taskPerLv[i] > 0) {
				// at this level all executors are assigned
				if (taskPerLv[i] >= exeNum) {
					assignment[i] += exeNum;
					taskPerLv[i] -= exeNum;
					exeNum = 0;
					return exeNum;
				}
				// all tasks are assigned, we move to the next lv
				else {
					assignment[i] += taskPerLv[i];
					exeNum -= taskPerLv[i];
					taskPerLv[i] = 0;
					continue;
				}
			}
		}
		//
		if (exeNum > 0) {
			
		}
		return exeNum;
	}
	
	public static void main(String[] args){
		//bfsAssign();
	}
}
