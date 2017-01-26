package com.yzeng.leetcode.easy;

import java.util.Stack;

import com.yzeng.datastructures.TreeNode;

public class MinDepthBTree {
//	public int minDepth(TreeNode root) {
//		if (root == null) {
//			return 0;
//		}
//		int depth = 1;
//		Stack<TreeNode> curLvStack = new Stack<TreeNode>();
//		Stack<TreeNode> nextLvStack = new Stack<TreeNode>();
//		curLvStack.push(root);
//		while (true) {
//			while (!curLvStack.isEmpty()) {
//				TreeNode current = curLvStack.pop();
//				TreeNode left = current.left, right = current.right;
//				if (left == null && right == null) {
//					return depth;
//				}
//				else{
//					if (left != null && right != null) {
//						nextLvStack.push(left);
//						nextLvStack.push(right);
//					}
//					else if (left == null){
//						nextLvStack.push(right);
//					}
//					else {
//						nextLvStack.push(left);
//					}
//				}
//			}
//			depth ++;
//			curLvStack.clear();
//			Stack<TreeNode> tmpStack = nextLvStack;
//			nextLvStack = curLvStack;
//			curLvStack = tmpStack;
//		}
//    }
	public int minDepth(TreeNode root) {
		if (root == null) {
			return 0;
		}
		int minLeft = minDepth(root.left), minRight = minDepth(root.right);
		return (1 + Math.max(minLeft, minRight));
	}
	
	public static void main(String[] args){
		TreeNode root = new TreeNode(1);
		root.left = new TreeNode(2);
		root.right = new TreeNode(3);
		root.left.right = new TreeNode(4);
		root.left.right.left = new TreeNode(5);
		new MinDepthBTree().minDepth(root);
	}
}
