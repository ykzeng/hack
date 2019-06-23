package com.yzeng.leetcode.hard;

public class LongestIncreasingPath {
//	public int longestIncreasingPath(int[][] matrix) {
//		if (matrix == null || matrix[0] == null) {
//			return 0;
//		}
//		int row = matrix.length, col = matrix[0].length, max = 0;
//        boolean[][] visited = new boolean[row][col];
//        for (int i = 0; i < row; i++) {
//			for (int j = 0; j < col; j++) {
//				visited[i][j] = false;
//			}
//		}
//        for (int i = 0; i < row; i++) {
//			for (int j = 0; j < col; j++) {
//				if (!visited[i][j]) {
//					int pathLen = recurPath(matrix, row, col, visited, i, j);
//					max = pathLen > max ? pathLen : max;
//				}
//			}
//		}
//        return max;
//    }
//	
//	public int recurPath(int[][] matrix, int row, int col, boolean[][] visited, int i, int j){
//		visited[i][j] = true;
//		int upIncr = 0, downIncr = 0, leftIncr = 0, rightIncr = 0, curElem = matrix[i][j], max = 0;
//		if (i - 1 >= 0 && matrix[i - 1][j] > curElem) {
//			upIncr = recurPath(matrix, row, col, visited, i - 1, j);
//			max = upIncr;
//		}
//		if (i + 1 < row && matrix[i + 1][j] > curElem) {
//			downIncr = recurPath(matrix, row, col, visited, i + 1, j);
//			max = downIncr > max ? downIncr : max;
//		}
//		if (j - 1 >= 0 && matrix[i][j - 1] > curElem) {
//			leftIncr = recurPath(matrix, row, col, visited, i, j-1);
//			max = leftIncr > max ? leftIncr : max;
//		}
//		if (j + 1 < col && matrix[i][j + 1] > curElem) {
//			rightIncr = recurPath(matrix, row, col, visited, i, j + 1);
//			max = rightIncr > max ? rightIncr : max;
//		}
//		return (max + 1);
//	}
	
	public int longestIncreasingPath(int[][] matrix) {
		if (matrix == null || matrix.length == 0 || matrix[0] == null) {
			return 0;
		}
		int row = matrix.length, col = matrix[0].length, max = 0;
        int[][] visited = new int[row][col];
        for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				visited[i][j] = -1;
			}
		}
        for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (visited[i][j] == -1) {
					int pathLen = recurPath(matrix, row, col, visited, i, j);
					max = pathLen > max ? pathLen : max;
				}
			}
		}
        return max;
    }
	
	public int recurPath(int[][] matrix, int row, int col, int[][] visited, int i, int j){
		if (visited[i][j] != -1) {
			return visited[i][j];
		}
		int upIncr = 0, downIncr = 0, leftIncr = 0, rightIncr = 0, curElem = matrix[i][j], max = 0;
		if (i - 1 >= 0 && matrix[i - 1][j] > curElem) {
			upIncr = recurPath(matrix, row, col, visited, i - 1, j);
			max = upIncr;
		}
		if (i + 1 < row && matrix[i + 1][j] > curElem) {
			downIncr = recurPath(matrix, row, col, visited, i + 1, j);
			max = downIncr > max ? downIncr : max;
		}
		if (j - 1 >= 0 && matrix[i][j - 1] > curElem) {
			leftIncr = recurPath(matrix, row, col, visited, i, j-1);
			max = leftIncr > max ? leftIncr : max;
		}
		if (j + 1 < col && matrix[i][j + 1] > curElem) {
			rightIncr = recurPath(matrix, row, col, visited, i, j + 1);
			max = rightIncr > max ? rightIncr : max;
		}
		visited[i][j] = max + 1;
		return (max + 1);
	}
	
	public static void main(String[] args){
		int[][] matrix = {{9, 9, 4}, 
						  {6, 6, 8},
						  {2, 1, 1}};
//		int[][] matrix = {{3, 4, 5}, 
//				  {3, 2, 6},
//				  {2, 2, 1}};
		System.out.println(new LongestIncreasingPath().longestIncreasingPath(matrix));
	}
}
