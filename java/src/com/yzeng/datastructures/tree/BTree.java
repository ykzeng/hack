package com.yzeng.datastructures.tree;

public class BTree{
	private TreeNode<Integer> root = null;
	
	public void printPostOrder(TreeNode<Integer> root){
		if (root == null) {
			return;
		}
		
		printPostOrder(root.left);
		printPostOrder(root.right);
		
		System.out.print(root.val + " ");
	}
	
	public void printInOrder(TreeNode<Integer> root){
		if (root == null) {
			return;
		}
		
		printInOrder(root.left);
		System.out.print(root.val + " ");
		printInOrder(root.right);
	}
	
	public void printPreOrder(TreeNode<Integer> root){
		if (root == null) {
			return;
		}
		
		System.out.print(root.val + " ");
		printPreOrder(root.left);
		printPreOrder(root.right);
	}
	
	// Wrappers over above recursive functions
    void printPostorder()  {     printPostOrder(root);  }
    void printInorder()    {     printInOrder(root);   }
    void printPreorder()   {     printPreOrder(root);  }
	
	// Driver method
    public static void main(String[] args)
    {
        BTree tree = new BTree();
        tree.root = new TreeNode<Integer>(1);
        tree.root.left = new TreeNode<Integer>(2);
        tree.root.right = new TreeNode<Integer>(3);
        tree.root.left.left = new TreeNode<Integer>(4);
        tree.root.left.right = new TreeNode<Integer>(5);
 
        System.out.println("Preorder traversal of binary tree is ");
        tree.printPreorder();
 
        System.out.println("\nInorder traversal of binary tree is ");
        tree.printInorder();
 
        System.out.println("\nPostorder traversal of binary tree is ");
        tree.printPostorder();
    }
}
