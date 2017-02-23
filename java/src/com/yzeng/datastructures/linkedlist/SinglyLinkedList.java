package com.yzeng.datastructures.linkedlist;

public class SinglyLinkedList <T> {
	private LNode<T> tail = null;
	private LNode<T> head = null;
	private int size = 0;
	
	public SinglyLinkedList(T data){
		LNode<T> lNode = new LNode<T>(data);
		this.head = lNode;
		this.tail = lNode;
		size = 1;
	}
	
	public int size(){
		return this.size;
	}
	
	public boolean isEmpty(){
		return this.size == 0;
	}
	
	public T first(){
		if (isEmpty()) {
			return null;
		}
		return this.head.val;
	}
	
	public T last(){
		if (isEmpty()) {
			return null;
		}
		return this.tail.val;
	}
	
	public void addFirst(T data){
		LNode<T> newNode = new LNode<T>(data);
		newNode.next = this.head;
		this.head = newNode;
		if (size ++ == 0) {
			this.tail = head;
		}
	}
	
	public void addLast(T data){
		LNode<T> lastNode = new LNode<T>(data);
		if (size ++ == 0) {
			this.head = lastNode;
			this.tail = lastNode;
		}
		else{
			this.tail.next = lastNode;
			this.tail = lastNode;
		}
	}
	
	public T removeFirst(){
		if (isEmpty()) {
			return null;
		}
		T data = this.head.val;
		this.head = this.head.next;
		this.size --;
		return data;
	}
}
