"""
https://www.geeksforgeeks.org/making-elements-distinct-sorted-array-minimum-increments/
"""
def min_incre1(arr):
	gap=[]
	redun=[]
	init_sum=sum(arr)
	for i in range(0, len(arr)):
		if arr[i]==arr[i-1]:
			redun.append(arr[i])
		elif arr[i]-arr[i-1]>1:
			for j in range(arr[i-1]+1, arr[i]):
				gap.append(j)

def min_incre(arr):
	for n in range(0, len(arr)):
		if n+1<len(arr) and arr[n+1]<=arr[n]:
			arr[n+1]=arr[n]+1
	return sum(arr)

test1=[2, 2, 3, 5, 6]
test2=[20, 20]
test3=[3, 4, 6, 8]
print min_incre(test3)