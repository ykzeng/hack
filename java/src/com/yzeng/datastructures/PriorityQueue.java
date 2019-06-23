package com.yzeng.datastructures;

public interface PriorityQueue<K, V> {
	int size();
	boolean isEmpty();
	KeyUpdatableEntry<K, V> insert(K key, V value);
	KeyUpdatableEntry<K, V> min();
	KeyUpdatableEntry<K, V> removeMin();
}
