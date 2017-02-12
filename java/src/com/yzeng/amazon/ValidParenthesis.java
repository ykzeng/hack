package com.yzeng.amazon;

import java.util.Stack;

public class ValidParenthesis {
	public boolean isValid(String s){
		char[] charArray = s.toCharArray();
		int pairs = 0;
		Stack<Character> stack = new Stack<Character>();
		for (int i = 0; i < charArray.length; i++) {
			char p = charArray[i];
			if (p == '(' || p == '[' || p == '{') {
				stack.push(p);
			}
			else if (!stack.isEmpty()){
				if (p == ')') {
					char last = stack.pop();
					if (last != '(')
						return false;
				}
				else if (p == '}' || p == ']') {
					char last = stack.pop();
					if (p != last + 2) 
						return false;
				}
				else
					return false;
			}
			else
				return false;
		}
		if (stack.isEmpty())
			return true;
		else
			return false;
	}
	
	public static void main(String[] args){
		String string = "()((()))()())))(((())))()";
		System.out.println(pureIsValid(string));
	}
	
	public static int pureIsValid(String s){
		int pair = 0;
		Stack<Character> stack = new Stack<Character>();
		for (int i = 0; i < s.length(); i++) {
			if (stack.isEmpty()) 
				stack.push(s.charAt(i));
			else if (stack.peek() == s.charAt(i) - 1) {
				stack.pop();
				pair ++;
			}
			else
				stack.push(s.charAt(i));
		}
		if (stack.isEmpty())
			return pair;
		else
			return -1;
	}
}
