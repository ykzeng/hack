from collections import Counter

def breakPalindrome(s):
	counter=Counter(s)
	if len(counter)==1:
		return "IMPOSSIBLE"
	arr=list(s)
	for i in range(0, len(arr)):
		if arr[i]!='a':
			arr[i]='a'
			break
	return ''.join(arr)

print breakPalindrome('bab')