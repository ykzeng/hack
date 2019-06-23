package com.yzeng.goldman;

import java.util.Scanner;

public class StringCompression {
	public static String compress(String input){
		char[] str_char = input.toCharArray();
		char prev = str_char[0];
		int rep = 1;
		String result = "", tmp_compressed = String.valueOf(prev);
		for (int i = 1; i < str_char.length; i++) {
			if (prev != str_char[i]){ 
				result += tmp_compressed;
				rep = 0;
				prev = str_char[i];
			}
			rep ++;
			tmp_compressed = String.valueOf(prev) + 
					(rep > 1 ? String.valueOf(rep) : "");
		}
		return (result + tmp_compressed);
	}
	
	public static void main(String[] args){
//		String tocompress = "abcaaabbb", result;
//		
//		result = compress(tocompress);
//		System.out.println("Original String: " + tocompress);
//		System.out.println("Compressed String: " + result);
		System.out.println("String to compress: ");
		Scanner sc = new Scanner(System.in);
		String input = sc.next();
		System.out.println("String compressed: ");
		System.out.println(compress(input));
		sc.close();
	}
}
