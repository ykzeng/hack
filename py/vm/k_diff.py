"""
K-diff Pairs in an Array
https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
"""
import collections

def findPairs1(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: int
	"""
	if k<0:
		return 0
	if k==0:
		return sum(v>1 for v in collections.Counter(nums).values())
	pair={}
	exist={}
	for num in nums:
		if num in exist:
			continue
		exist[num]=True
		if (num+k) in pair:
			pair[num+k]+=1
		else:
			pair[num+k]=1
	#print pair
	count=0
	for num in nums:
		if num in pair:
			count+=pair[num]
	return count

def findPairs(nums, k):
    res = 0
    c = collections.Counter(nums)
    print c
    for i in c:
        if k > 0 and i + k in c or k == 0 and c[i] > 1:
            res += 1
    return res

test1=[3, 1, 4, 1, 5]
k1=2
print findPairs(test1, k1)

test2=[1, 2, 3, 4, 5]
k2=1
print findPairs(test2, k2)

test3=[1, 3, 1, 5, 4]
k3=0
print findPairs(test3, k3)