package com.yzeng.leetcode.easy;

import com.yzeng.datastructures.TreeNode;

public class LeftLeavesSum {
	
	public int sumOfLeftLeaves(TreeNode root) {
		int sum = 0;
		if (root == null) {
			return 0;
		}
		if (root.left != null) {
			if (root.left.left == null && root.left.right == null) {
				sum += root.left.val;
			}
			else {
				sum += sumOfLeftLeaves(root.left);
			}
		}
		sum += sumOfLeftLeaves(root.right);
		return sum;
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
