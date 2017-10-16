package com.yzeng.goldman;

import java.util.Collection;
import java.util.HashMap;
import java.util.Iterator;

public class ValidAnagram {
	public static boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> charMap = new HashMap<Character, Integer>();
        Character tmp_char = ' ';
        Integer tmp_count = 0;
        for (int i = 0; i < s.length(); i ++) {
            tmp_char = s.charAt(i);
            tmp_count = charMap.get(tmp_char);
            tmp_count = tmp_count == null ? 0 : tmp_count;
            charMap.put(tmp_char, (tmp_count+1));
        }
        for (int i = 0; i < t.length(); i ++) {
            tmp_char = t.charAt(i);
            tmp_count = charMap.get(tmp_char);
            tmp_count = tmp_count == null ? 0 : tmp_count;
            if (tmp_count == 0)
                return false;
            
            charMap.put(tmp_char, (tmp_count-1));
        }
        Collection collection = charMap.values();
        Iterator iterator = collection.iterator();
        while (iterator.hasNext()) {
        	if (((Integer)iterator.next()) != 0) {
				return false;
			}
		}
        return true;
    }
	
	public static void main(String[] args){
		String s = "a", t = "a";
		System.out.println(isAnagram(s, t));
	}
}
