package com.yzeng.datastructures;

import java.util.ArrayList;

public class HeapPriorityQueue<K, V> extends AbstractPriorityQueue<K, V> {
	private ArrayList<KeyUpdatableEntry<K, V>> heap;
	
	@Override
	public int size() {
		// TODO Auto-generated method stub
		return heap.size();
	}

	protected int parent(int child){return (child - 1) / 2;}
	
	protected int leftChild(int parent){return parent * 2;}
	
	protected int rightChild(int parent){return parent * 2 + 1;}
	
	protected boolean hasLeftChild(int parent){return (leftChild(parent) < heap.size());}
	
	protected boolean hasRightChild(int parent){return (rightChild(parent) < heap.size());}
	
	protected void upHeap(int startIndex){
		int i = startIndex;
		while (i >= 0) {
			int parentIndex = parent(i);
			if (compare(heap.get(i), heap.get(parentIndex)) < 0) {
				swap(i, parentIndex);
				i = parentIndex;
			}
			else break;
		}
	}
	
	protected void downHeap(int startIndex){
		int i = startIndex;
		while (i < heap.size()) {
			int left = -1, right = -1, indexToGo = -1;
			if (!hasLeftChild(i)) break;
			// only has left child, no right
			else if (!hasRightChild(i)) {
				left = rightChild(i);
				indexToGo = left;
			}
			// both left and right
			else {
				left = leftChild(i);
				right = rightChild(i);
				indexToGo = compare(heap.get(left), heap.get(right)) < 0 ? left : right;
			}
			// compare keys between the current parent and the min key among its children and swap if neccessary
			if (compare(heap.get(indexToGo), heap.get(i)) < 0) {
				swap(indexToGo, i);
				i = indexToGo;
			}
			else break;
		}
	}
	
	protected void swap(int index1, int index2){
		KeyUpdatableEntry<K, V> tempEntry = heap.get(index1);
		heap.set(index1, heap.get(index2));
		heap.set(index2, tempEntry);
	}
	
	@Override
	public KeyUpdatableEntry<K, V> insert(K key, V value) {
		// TODO Auto-generated method stub
		KeyUpdatableEntry<K, V> newEntry = new PQEntry<K, V>(key, value);
		heap.add(newEntry);
		upHeap(heap.size() - 1);
		return newEntry;
	}

	@Override
	public KeyUpdatableEntry<K, V> min() {
		// TODO Auto-generated method stub
		return heap.get(0);
	}

	@Override
	public KeyUpdatableEntry<K, V> removeMin() {
		// TODO Auto-generated method stub
		KeyUpdatableEntry<K, V> min = heap.get(0);
		heap.set(0, heap.get(heap.size() - 1));
		heap.remove(heap.size() - 1);
		downHeap(0);
		return min;
	}
	
}
