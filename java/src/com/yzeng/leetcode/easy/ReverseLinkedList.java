package com.yzeng.leetcode.easy;

import com.yzeng.datastructures.linkedlist.ListNode;

public class ReverseLinkedList {
	public static void main(String[] args){
		ListNode head = new ListNode(1);
		ListNode p = head;
		for (int i = 2; i < 10; i++) {
			p.next = new ListNode(i);
			p = p.next;
		}
		p = new ReverseLinkedList().reverseList(head);
		p.printAll();
	}
	
//	public ListNode reverseList(ListNode head) {
//		if (head == null) {
//			return null;
//		}
//		ListNode result = head, p;
//		head = head.next;
//		result.next = null;
//		while (head != null) {
//			p = head;
//			head = head.next;
//			p.next = result;
//			result = p;
//		}
//		return result;
//    }
	
	
//	public ListNode reverseList(ListNode head){
//		ListNode result = null;
//		while(head != null){
//			ListNode p = head;
//			head = head.next;
//			p.next = result;
//			result = p;
//		}
//		return result;
//	}
	
	public ListNode reverseList(ListNode head){
		return backAdd(head, null);
	}
	
	public ListNode backAdd(ListNode head, ListNode result){
		if (head == null) {
			return result;
		}
		ListNode pListNode = head;
		head = head.next;
		pListNode.next = result;
		result = pListNode;
		return backAdd(head, result);
	}
}
