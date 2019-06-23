package com.yzeng.amazon;

public class RotateMatrix {
	public static void main(String[] args){
		int[][] matrix = new int[3][4];
		int count = 0;
		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix[0].length; j++) {
				count ++;
				matrix[i][j] = count;
			}
		}
		RotateMatrix rMatrix = new RotateMatrix();
		System.out.println("Original matrix: ");
		rMatrix.printMatrix(matrix);
		int[][] result = rMatrix.rotateMatrix(matrix);
		System.out.println("Rotated: ");
		rMatrix.printMatrix(result);
		System.out.println("AntiRotated: ");
		result = rMatrix.diagonalShuffle(result);
		rMatrix.printMatrix(result);
	}
	
	public int[][] rotateMatrix(int[][] matrix){
		int[][] result = new int[matrix[0].length][matrix.length];
		for (int i = 0; i < matrix.length; i++) {
			int[] row = matrix[i];
			for (int j = 0; j < matrix[0].length; j++) {
				result[j][matrix.length - i - 1] = row[j];
			}
		}
		return result;
	}
	
	public int[][] diagonalShuffle(int[][] matrix){
		int row = matrix.length, col = matrix[0].length;
		int[][] result = new int[matrix.length][matrix[0].length];
		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				result[row - i - 1][col - j - 1] = matrix[i][j];
			}
		}
		return result;
	}
	
	public void printMatrix(int[][] matrix){
		for (int i = 0; i < matrix.length; i++) {
			for (int j = 0; j < matrix[0].length; j++) {
				System.out.print(matrix[i][j] + " ");
			}
			System.out.println();
		}
	}
}
