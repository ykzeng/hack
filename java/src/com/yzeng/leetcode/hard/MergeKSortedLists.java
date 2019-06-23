package com.yzeng.leetcode.hard;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Random;

import com.yzeng.datastructures.linkedlist.ListNode;

public class MergeKSortedLists {
	static class NodeComparator implements Comparator<ListNode>{
		@Override
		public int compare(ListNode o1, ListNode o2) {
			// TODO Auto-generated method stub
			if (o1.val > o2.val) {
				return 1;
			}
			else
				return -1;
		}
		
	}
	
	public static ListNode mergeKLists(ListNode[] lists) {
		if (lists != null && lists.length == 0) {
			return null;
		}
        PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>(new NodeComparator());
        ListNode listNode = null;
        for (int i = 0; i < lists.length; i++) {
        	if (lists[i] != null) {
    			queue.add(lists[i]);
			}
		}
        listNode = new ListNode(queue.poll().val);
        while (!queue.isEmpty()) {
			ListNode tempNode = queue.poll();
			listNode.next = tempNode;
			if (tempNode.next != null) {
				queue.add(tempNode.next);	
			}
		}
        return listNode;
    }
	
	public static void main(String[] args){
		Random random = new Random();
		ListNode[] listNodes = new ListNode[5];
		for (int i = 0; i < 5; i++) {
			ListNode node = new ListNode(0);
			ListNode p = node;
			for (int j = 0; j < 10; j++) {
				node.val = random.nextInt(100);
				node.next = new ListNode(0);
				node = node.next;
			}
			listNodes[i] = p;
		}
		mergeKLists(listNodes);
	}
}
