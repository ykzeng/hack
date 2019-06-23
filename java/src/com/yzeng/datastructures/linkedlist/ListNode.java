package com.yzeng.datastructures.linkedlist;

public class ListNode{
	public int val;
	public ListNode next;
	
	public ListNode(int x) {
		// TODO Auto-generated constructor stub
		this.val = x;
	}
	
	public void printAll(){
		ListNode p = this;
		while (p != null) {
			System.out.println(p.val);
			p = p.next;
		}
	}
}
