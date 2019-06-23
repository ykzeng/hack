package com.yzeng.hack.btreeinvert;

import java.util.Stack;

public class Solution {
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void invertBinaryTree(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
    	stack.push(root);
        
        while(!stack.isEmpty()){
        	TreeNode current = stack.pop();
        	if ((current.left != null) || (current.right != null)){
            	TreeNode tmpLeft = current.left;
            	current.left = current.right;
            	current.right = tmpLeft;
            	if (current.left != null) {
					stack.push(current.left);
				}
            	if (current.right != null) {
					stack.push(current.right);
				}
            }
        }
    }
    
    public static void main(String[] args){
    	TreeNode root = new TreeNode(1);
    	
    	root.left = new TreeNode(2);
    	root.right = new TreeNode(3);
    	root.left.left = new TreeNode(4);
    	root.left.right = new TreeNode(5);
    	root.right.left = new TreeNode(6);
    	root.right.right = new TreeNode(7);
    	
    	(new Solution()).invertBinaryTree(root);
    }
}
