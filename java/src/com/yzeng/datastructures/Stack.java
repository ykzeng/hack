package com.yzeng.datastructures;

import com.yzeng.datastructures.linkedlist.LNode;

public class Stack <T> {
	private LNode<T> head;
	
	public Stack(T data){
		head = new LNode<T>(data);
	}
	
	public Stack(){
		head = null;
	}
	
	public boolean isEmpty(){
		return (head == null);
	}
	
	public T pop(){
		if (!isEmpty()) {
			T data = head.val;
			head = head.next;
			return data;
		}
		else
			return null;
	}
	
	public T peek(){
		return head == null ? null : head.val;
	}
	
	public void push(T data){
		LNode<T> newNode = new LNode<T>(data);
		newNode.next = head;
		head = newNode;
	}
}
