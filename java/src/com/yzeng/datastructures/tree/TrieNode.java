package com.yzeng.datastructures.tree;

public class TrieNode {
	public TrieNode[] children = null;
	public int freq;
	
	public TrieNode(){
		this.children = new TrieNode[26];
		this.freq = 0;
	}
}
