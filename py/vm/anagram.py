def main(str_arr1, str_arr2):
	arr=[0]*len(str_arr1)
	for i in range(0, len(str_arr1)):
		arr[i]=get_min_diff(str_arr1[i], str_arr2[i])
	return arr

def get_min_diff(str1, str2):
	if len(str1)!=len(str2):
		return -1
	base=ord('a')
	count_arr1=[0]*26
	count_arr2=[0]*26
	for c in str1:
		index=ord(c)-base
		count_arr1[index]+=1
	for c in str2:
		index=ord(c)-base
		count_arr2[index]+=1
	tot_rep=0
	for i in range(0, len(count_arr1)):
		if count_arr1[i]>count_arr2[i]:
			tot_rep+=(count_arr1[i]-count_arr2[i])
	return tot_rep

a = ['a','jk','abb','mn','abc']
b = ['bb','kj','bbc','op','def']
print main(a, b)

"""
We define an anagram to be a word whose characters can be rearranged to create another word. Given two strings, we want to know the minimum number of characters in either string that we must modify to make the two strings anagrams . If it's not possible to make the two strings anagrams, we consider this number to be -1.

For example:
tea and ate are anagrams, so we would need to modify 0 characters.
tea and toe are not anagrams, but we can modify 1 character in either string (o-> a or a-> o) to make them anagrams.
act and acts are not anagrams and cannot be converted to anagrams because they contain different numbers of characters.

Function Description 
Complete the function getMinimumDifference in the editor below. The function must return an array of integers which denote the minimum number of characters in either string that need to be modified to make the two strings anagrams. If it's not possible, return -1.

getMinimumDifference has the following parameter(s):
    a:  the first string
    b:  the second string

Constraints
Each string consists of lowercase characters [a-z].-google 1point3acres
1 <= n <= 100
0 <= |a|, |b| <= 104
1 <= |a| + |b| <= 104

Input Format for Custom Testing
Input is read from stdin and passed to the function.

The first line contains an integer n, the number of strings in the array a.
The n subsequent lines each contain a string describing ai where 0 <= i < n.
The next line contains an integer n, the number of strings in the array b.
The n subsequent lines each contain a string describing bi where 0 <= i < n.

Sample Case 0

Sample Input For Custom Testing
a = {'a','jk','abb','mn','abc'} 
b = {'bb','kj','bbc','op','def'
Sample Output
-1
0
1
2
3
Explanation
Given a = [a, jk, abb, mn, abc] and b = [bb, kj, bbc, op, def], we perform the following n = 5 calculations:
Index 0: a and bb cannot be anagrams because they contain different numbers of characters.
Index 1: jk and kj are already anagrams because they both contain the same characters at the same frequencies
Index 2: abb and bbc differ by one character.
Index 3: mn and op differ by two characters.
Index 4: abc and def differ by three characters.
After checking each pair of strings, we return the array [-1, 0, 1, 2, 3] as our answer.

visit 1point3acres for more.
"""