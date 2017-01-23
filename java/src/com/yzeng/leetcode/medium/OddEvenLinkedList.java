package com.yzeng.leetcode.medium;

import java.awt.List;

import com.yzeng.datastructures.ListNode;

public class OddEvenLinkedList {
	// my original answer
//	public ListNode oddEvenList(ListNode head) {
//		if (head == null || head.next == null) {
//			return head;
//		}
//		ListNode p = head, pOddEnd = p, pEven = p.next, pEvenEnd = pEven;
//		boolean finish = false;
//		p = p.next.next;
//		// init the foremost two nodes
//		while (p != null) {
//			pOddEnd.next = p;
//			pEvenEnd.next = p.next;
//			if (p.next != null) {
//				p = p.next.next;
//			}
//			else
//				finish = true;
//			
//			pOddEnd = pOddEnd.next;
//			pOddEnd.next = pEven;
//			
//			if (!finish) {
//				pEvenEnd = pEvenEnd.next;
//				pEvenEnd.next = null;
//			}
//			else
//				return head;
//		}
//		return head;
//    }
	
//	public ListNode oddEvenList(ListNode head){
//		if (head == null || head.next == null) {
//			return head;
//		}
//		ListNode p = head.next.next, pOdd = head, pEven = head.next, pEvenLast = pEven;
//		while (p != null) {
//			pOdd.next = p;
//			p = p.next;
//			pOdd = pOdd.next;
//			pOdd.next = pEven;
//			if (p == null) {
//				pEvenLast.next = null;
//				return head;
//			}
//			pEvenLast.next = p;
//			p = p.next;
//			pEvenLast = pEvenLast.next;
//			pEvenLast.next = null;
//		}
//		return head;
//	}
	// editorial solution
	public ListNode oddEvenList(ListNode head) {
	    if (head != null) {
	    
	        ListNode odd = head, even = head.next, evenHead = even; 
	    
	        while (even != null && even.next != null) {
	            odd.next = odd.next.next; 
	            even.next = even.next.next; 
	            odd = odd.next;
	            even = even.next;
	        }
	        odd.next = evenHead; 
	    }
	    return head;
	}
	
	public static void main(String[] args){
		ListNode node = new ListNode(1), p = node;
		for (int i = 2; i <= 3; i++) {
			node.next = new ListNode(i);
			node = node.next;
		}
		System.out.println(new OddEvenLinkedList().oddEvenList(p));
	}
}
