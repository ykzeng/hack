package com.yzeng.datastructures.tree;

public class Trie {
	private TrieNode root;
	
	public Trie(){
		root = new TrieNode();
	}
	
	public void insert(String word){
		char[] wordChar = word.toCharArray();
		TrieNode node = root;
		for (int i = 0; i < wordChar.length; i++) {
			int index = wordChar[i] - 'a';
			if(node == null){
				node = new TrieNode();
				node.children[index] = new TrieNode();
			}
			node = node.children[index];
			
			if (i == (wordChar.length - 1)) {
				node.freq ++;
			}
		}
	}
	
	public int search(String word){
		char[] wordChar = word.toCharArray();
		TrieNode node = root;
		for(int i = 0; i < wordChar.length; i++){
			int index = wordChar[i] - 'a';
			if (node.children == null) 
				return -1;
			else
				node = node.children[index];
		}
		return node.freq;
	}
	
	public static void main(String[] args){
		Trie trie = new Trie();
		trie.insert("avalon");
		
		trie.insert("yangyang");
		trie.insert("yangyang");
		trie.insert("yang");
		
		trie.insert("yukun");
		trie.insert("yukunzeng");
		
		System.out.println("search yukun freq in trie: " + trie.search("yukun"));
		System.out.println("search yuku freq in trie: " + trie.search("yuku"));
		System.out.println("search yangyang freq in trie: " + trie.search("yangyang"));
	}
}
