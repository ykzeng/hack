package com.yzeng.leetcode.easy;

import com.yzeng.datastructures.TreeNode;

public class LeftLeavesSum {
	
	public int sumOfLeftLeaves(TreeNode root) {
		if (root == null) {
			return 0;
		}
		int leftSum = 0;
		leftSum = traverse(root);
		return leftSum;
    }
	
	public int traverse(TreeNode root){
		int leftSum = 0;
		if (root.right != null) {
			leftSum += traverse(root.right);
		}
		if (root.left != null) {
			leftSum += root.left.val;
			leftSum += traverse(root.left);
		}
		return leftSum;
	}
	
	public static void main(String[] args){
		TreeNode root = new TreeNode(1);
		TreeNode pNode = root;
		pNode.left = null;
		
		pNode.right = new TreeNode(2);
		pNode.right.right = new TreeNode(3);
		pNode.right.right.left = new TreeNode(4);
		pNode.right.right.right = new TreeNode(5);
		
		System.out.println(new LeftLeavesSum().sumOfLeftLeaves(root));
	}
}
