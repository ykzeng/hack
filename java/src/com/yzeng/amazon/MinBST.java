package com.yzeng.amazon;

import com.yzeng.datastructures.tree.TreeNode;

public class MinBST {
	public static void main(String[] args){
		
	}
	
	public static int minBST(TreeNode<Integer> tNode){
//		if (tNode.left != null && tNode.right != null) {
//			int leftTotal = minBST(tNode.left), rightTotal = minBST(tNode.right);
//			return ((leftTotal > rightTotal ? rightTotal : leftTotal) + tNode.val);
//		}
//		else if (tNode.left == null && tNode.right == null) {
//			return tNode.val;
//		}
//		else {
//			return minBST(tNode.left == null ? tNode.right : tNode.left);
//		}
		if (tNode == null) 
			return 0;
		else if (tNode.left == null && tNode.right == null) 
			return tNode.val;
		else if (tNode.left != null && tNode.right != null){
			int leftTotal = minBST(tNode.left), rightTotal = minBST(tNode.right);
			return ((leftTotal > rightTotal ? rightTotal : leftTotal) + tNode.val);
		}
		else
			return minBST(tNode.left == null ? tNode.right : tNode.left) + tNode.val;
	}
}
