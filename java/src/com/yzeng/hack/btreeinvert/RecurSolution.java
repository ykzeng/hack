package com.yzeng.hack.btreeinvert;

public class RecurSolution {
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    public void invertBinaryTree(TreeNode root) {
        // write your code here
    	if (root.left != null) {
			invertBinaryTree(root.left);
		}
    	if (root.right != null) {
			invertBinaryTree(root.right);
		}
    	TreeNode tmpLeft = root.left;
    	root.left = root.right;
    	root.right = tmpLeft;
    	return;
    	
//        while((root.left != null) && (root.right != null)){
//        	invertBinaryTree(root.left);
//        	
//        	TreeNode tmpLeft = root.left;
//        	root.left = root.right;
//        	root.right = tmpLeft;
//        }
    }
}
