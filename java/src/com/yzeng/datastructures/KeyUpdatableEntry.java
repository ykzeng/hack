package com.yzeng.datastructures;

public interface KeyUpdatableEntry<K, V> {
	public K getKey();
	
	public void setKey(K key);

	public V getValue();
	
	public void setValue(V value);
}
