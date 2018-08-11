def longest_even(str1):
	str_arr=str1.split(' ')
	even_str=''
	for s in str_arr:
		if len(s)%2==0:
			if len(s)>len(even_str):
				even_str=s
	return even_str

test1="It is a pleasant day today"
print longest_even(test1)

test2="You can do it the way you like"
print longest_even(test2)

"""
Consider a string, sentence, of space-separated words where each word is a substring consisting of English alphabetic letters only. We want to find the first word in sentence having a length which is both an even number and greater than or equal to the length of any other word of even length in the sentence.

For example, if sentence is Time to write great code, then the word we're looking for is Time. While code and Time are of maximal length, Time occurs first. If sentence is Write code for a great time, then the word we're looking for is code.

Function Description 
Complete the function longestEvenWord in the editor below. The function must return the word (string) that is the first occurrence of a string with maximal even number length. If there are no even length words, return 00.
longestEvenWord has the following parameter(s):
    sentence:  a sentence string

Constraints
1 <= |sentence| <= 105
The sentence string consists of spaces and characters in the ranges ascii[a-z, A-Z] only.

Input Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

A single line of space-separated strings denoting sentence

Sample Case 0
Sample Input 0
It is a pleasant day today.

Sample Output 0
pleasant

Explanation 0
The sentence has three even length words: It (with length 2), is (2), and pleasant (8).

Sample Case 1
Sample Input 1
You can do it the way you like

Sample Output 1
like

Explanation 1
The sentence has three even length words: do (with length 2), it (2), and like (4).

.. 1point 3acres
"""