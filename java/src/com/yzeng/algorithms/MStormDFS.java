package com.yzeng.algorithms;

import java.util.Arrays;
import java.util.HashMap;

public class MStormDFS {
	public static boolean dfsAssign(int [] exptExecutorsOfDevice, String[] compNames, 
			HashMap<String, Integer> compName2TaskNum, int[][] assignment){
		int[] exeOnDevice = exptExecutorsOfDevice.clone(), taskPerLv;
		// task number for each component
		// get the task count of multi level components respectively
		taskPerLv = new int[compNames.length];
		for (int i = 0; i < compNames.length; i++) {
			taskPerLv[i] = compName2TaskNum.get(compNames[i]);
		}
		return dfsAssign(exeOnDevice, taskPerLv, assignment);
	}
	
	public static boolean dfsAssign(int[] exeOnDevice, int[] taskOnComp, int[][] assignment){
		int[] taskPerLv = taskOnComp.clone();
		int exeNum = 0, rootLv = 0; 
		for (int i = 0; i < exeOnDevice.length; i++) {
			exeNum = exeOnDevice[i];
			for (int j = 0; j < taskPerLv.length; j++) {
				if (taskPerLv[j] > 0) {
					rootLv = j;
					break;
				}
			}
			// if after doing dfs on the root level, we still have more executors
			// we assign as many root-lv nodes to the device as we can
			// theorem: 1. after dfs from the rootLv, if there are executors remained,
			// all nodes at following level must have been assigned
			// 2. per our rootlv selection strategy, there are no more tasks in the previous level
			int remainingExe = dfs(rootLv, exeNum, taskPerLv, assignment[i]);
			if (remainingExe > 0) {
				return true;
			}
			else if (remainingExe == 0) {
				if (i == exeOnDevice.length) {
					return true;
				}
			}
		}
		return false;
	}
	
	
	
	public static int dfs(int rootLv, int exeNum, int[] taskPerLv, int[] assignment){
		if (rootLv >= taskPerLv.length || taskPerLv[rootLv] <= 0 || exeNum == 0) {
			return exeNum;
		}
		// be noticed that if we entered dfs here, there must be at least one task to assign in root level
		int curLvCount = taskPerLv[rootLv];
		// visit every task in current level in order, only do dfs on the first task is enough
		exeNum --;
		assignment[rootLv] ++;
		taskPerLv[rootLv] --;
		exeNum = dfs(rootLv + 1, exeNum, taskPerLv, assignment);
		if (exeNum == 0) {
			return 0;
		}
		for (int i = 1; i < curLvCount; i++) {
			exeNum --;
			assignment[rootLv] ++;
			taskPerLv[rootLv] --;
		}
		return exeNum;
	}
	
	public static void main(String[] args){
		// passed
		//int[] exeOnDevice = {5, 2, 4, 3, 4}, taskPerLv = {3, 4, 3, 4, 2};
		//passed
		//int[] exeOnDevice = {2, 5, 4, 6}, taskPerLv = {5, 4, 2, 2};
		//passed
		int[] exeOnDevice = {6, 5, 4, 3, 3}, taskPerLv = {4, 4, 4, 3, 2};
		int[][] assignment = new int[exeOnDevice.length][taskPerLv.length];
		for (int i = 0; i < assignment.length; i++) {
			Arrays.fill(assignment[i], 0);
		}
		boolean ret = dfsAssign(exeOnDevice, taskPerLv, assignment);
		System.out.println(ret);
	}
}
