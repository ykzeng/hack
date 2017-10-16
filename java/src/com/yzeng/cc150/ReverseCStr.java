package com.yzeng.cc150;

public class ReverseCStr {
	public static String reverse1(String string){
		int length = string.length() - 1;
		char[] charStr = string.toCharArray();
		for (int i = 0; i < (length / 2); i++) {
			char temp = charStr[i];
			charStr[i] = charStr[length - 1 - i];
			charStr[length - 1 - i] = temp;
		}
		string = new String(charStr);
		return string;
	}
	
//	public String reverse2(String string){
//		
//	}
	public static void main(String args[]){
		//String string = "wo lei lajij";
		String string = "wo lei lajiij";
		System.out.println("String to reverse:");
		System.out.println(string);
		string = reverse1(string);
		System.out.println("String reversed: ");
		System.out.println(string);
	}
}
