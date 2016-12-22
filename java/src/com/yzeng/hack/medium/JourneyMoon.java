package com.yzeng.hack.medium;

import java.util.ArrayList;
import java.util.Scanner;

public class JourneyMoon {
	public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int pairCount = in.nextInt();
		
		ArrayList<ArrayList<Integer>> adjList = new ArrayList<ArrayList<Integer>>();
		// we define not visited as 0, visiting as 1, visited as 2
		int[] vertex_status = new int[n];
		for (int i = 0; i < n; i++) {
			vertex_status[i] = 0;
			adjList.add(new ArrayList<Integer>());
		}
		
		for (int i = 0; i < pairCount; i++) {
			int u = in.nextInt(), v = in.nextInt();
			adjList.get(u).add(v);
			adjList.get(v).add(u);
		}
		
		ArrayList<ArrayList<Integer>> dfsTrees = new ArrayList<ArrayList<Integer>>();
		for (int i = 0; i < vertex_status.length; i++) {
			if (vertex_status[i] == 0) {
				ArrayList<Integer> dfsTree = new ArrayList<Integer>();
				dfs(i, adjList, vertex_status, dfsTree);
				dfsTrees.add(dfsTree);
			}
		}
		
		long totalCombination = 0;
//		for (int i = 0; i < dfsTrees.size(); i++) {
//			for (int j = i + 1; j < dfsTrees.size(); j++) {
//				totalCombination += dfsTrees.get(i).size() * dfsTrees.get(j).size();
//			}
//		}
		for (int i = 0; i < dfsTrees.size(); i++) {
			totalCombination += dfsTrees.get(i).size();
		}
		totalCombination = (long)Math.pow(totalCombination, 2);
		for (int i = 0; i < dfsTrees.size(); i++) {
			totalCombination -= (long)Math.pow(dfsTrees.get(i).size(), 2);
		}
		totalCombination = totalCombination / 2;
		System.out.println(totalCombination);
	}
	
	public static void dfs(int root, ArrayList<ArrayList<Integer>> adjList, int[] vertexStatus, ArrayList<Integer> dfsTree){
		vertexStatus[root] = 1;
		dfsTree.add(root);
		ArrayList<Integer> curAdjList = adjList.get(root);
		for (int j = 0; j < curAdjList.size(); j++) {
			int vertex = curAdjList.get(j);
			// if not visited
			if (vertexStatus[vertex] == 0) {
				dfs(vertex, adjList, vertexStatus, dfsTree);
			}
		}
		vertexStatus[root] = 2;
	}
}
