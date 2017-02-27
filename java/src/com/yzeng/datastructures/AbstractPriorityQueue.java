package com.yzeng.datastructures;

import java.util.Comparator;

public abstract class AbstractPriorityQueue<K, V> implements PriorityQueue<K, V> {
	protected static class PQEntry<K, V> implements KeyUpdatableEntry<K, V>{
		private K key;
		private V value;
		
		public PQEntry(K key, V value) {
			// TODO Auto-generated constructor stub
			this.key = key;
			this.value = value;
		}
		
		@Override
		public K getKey() {
			// TODO Auto-generated method stub
			return this.key;
		}

		@Override
		public void setKey(K key) {
			// TODO Auto-generated method stub
			this.key = key;
		}

		@Override
		public V getValue() {
			// TODO Auto-generated method stub
			return this.value;
		}

		@Override
		public void setValue(V value) {
			// TODO Auto-generated method stub
			this.value = value;
		}
	}
	
	private Comparator<K> comparator;
	
	public AbstractPriorityQueue(Comparator<K> comparator){
		this.comparator = comparator;
	}
	
	public AbstractPriorityQueue(){
		this(new DefaultComparator<K>());
	}
	
	protected int compare(KeyUpdatableEntry<K, V> entry1, KeyUpdatableEntry<K, V> entry2){
		return this.comparator.compare(entry1.getKey(), entry2.getKey());
	}
	
	public boolean isEmpty(){return size() == 0;}
}
