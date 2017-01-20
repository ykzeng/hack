package com.yzeng.leetcode.medium;

import java.util.Scanner;

import com.yzeng.datastructures.ListNode;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class AddTwoNumbers {

    static int carry = 0, real_digit = 0;
	
	public static void main(String[] args){
		Scanner scanner = new Scanner(System.in);
		
		String line = scanner.nextLine();
		String[] line1Array = line.replaceAll("\\[", "").replaceAll("\\]", "").split(",");
		ListNode l1 = new ListNode(Integer.valueOf(line1Array[0]));
		ListNode p1 = l1;
		for (int i = 1; i < line1Array.length; i++) {
			p1.next = new ListNode(Integer.valueOf(line1Array[i]));
			p1 = p1.next;
		}
		
		line = scanner.nextLine();
		String[] line2Array = line.replaceAll("\\[", "").replaceAll("\\]", "").split(",");
		ListNode l2 = new ListNode(Integer.valueOf(line2Array[0]));
		ListNode p2 = l2;
		for (int i = 1; i < line2Array.length; i++) {
			p2.next = new ListNode(Integer.valueOf(line2Array[i]));
			p2 = p2.next;
		}
		ListNode l3 = addTwoNumbers(l1, l2);
		System.out.print(l3.val + " ");
		while (l3.next != null) {
			l3 = l3.next;
			System.out.print(l3.val + " ");
		}
	}
	
    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l3 = new ListNode(0);
        ListNode p3 = l3;
        
        calculateNext(l1, l2, null);
		l3.val = real_digit;
        
    	while ((l1.next != null) && ((l2.next) != null)) {
			l1 = l1.next;
			l2 = l2.next;
			calculateNext(l1, l2, l3);
			l3 = l3.next;
		}
    	
    	if (l1.next == null && l2.next == null);
    	else if (l1.next == null) {
			while (l2.next != null) {
				calculateNext(null, l2.next, l3);
				l3 = l3.next;
				l2 = l2.next;
			}
		}
    	else {
			while(l1.next != null){
				calculateNext(l1.next, null, l3);
				l3 = l3.next;
				l1 = l1.next;
			}
		}
    	
    	if (carry > 0) {
			l3.next = new ListNode(carry);
		}
    	
    	return p3;
    }
    
    public static void calculateNext(ListNode l1, ListNode l2, ListNode l3){
        int l1_digit = 0, l2_digit = 0, sum = 0;
    	if (l1 == null)
			l1_digit = 0;
		else
			l1_digit = l1.val;
		
		if (l2 == null) 
			l2_digit = 0;
		else
			l2_digit = l2.val;
		sum = l1_digit + l2_digit;
		real_digit = carry + sum;
		
		if (real_digit > 9) {
			carry = 1;
			real_digit = real_digit % 10;
		}
		else
			carry = 0;
		
		if (l3 != null) {
			ListNode newNode = new ListNode(real_digit);
			l3.next = newNode;
		}
    }
}