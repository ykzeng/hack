package com.yzeng.amazon;

import com.yzeng.datastructures.linkedlist.ListNode;

public class Reverse2ndHalfList {
	public static void main(String[] args){
		ListNode node = new ListNode(1), p = node;
		for (int i = 2; i < 10; i++) {
			node.next = new ListNode(i);
			node = node.next;
		}
		p.printAll();
		node = reverse2ndHalfList(p);
		node.printAll();
	}
	
	public static ListNode reverse2ndHalfList(ListNode head){
		if (head == null || head.next == null) {
			return head;
		}
		ListNode fastP = head, slowP = head;
		while (fastP.next != null && fastP.next.next != null) {
			fastP = fastP.next.next;
			slowP = slowP.next;
		}
		ListNode cur = slowP.next, newList = null, p;
		while (cur != null) {
			p = cur;
			cur = cur.next;
			p.next = newList;
			newList = p;
		}
		slowP.next = newList;
		return head;
	}
}
