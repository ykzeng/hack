package com.yzeng.ms;

import com.yzeng.datastructures.tree.TreeNode;

public class SearchBTree <T> {
	public T search(TreeNode<T> root, T target){
		// recursive
		T tmp;
		if(root == null)
			return null;
		if(target == root.val)
			return root.val;
		else{
			tmp = search(root.left, target);
			if (tmp != null) {
				return tmp;
			}
			else
				return search(root.right, target);
		}
	}
	
	public static void main(String[] args){
		TreeNode<String> tree = new TreeNode<String>("0-root");
		tree.left = new TreeNode<String>("1-left");
		tree.right = new TreeNode<String>("1-right");
		
		tree.left.left = new TreeNode<String>("1-left-2-left");
		tree.left.right = new TreeNode<String>("laji");
		tree.left.right.left = new TreeNode<String>("test");
		
		SearchBTree<String> bTree = new SearchBTree<String>();
		String result = bTree.search(tree, "test");
		System.out.println(result);
	}
}
