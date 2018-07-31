"""
https://www.geeksforgeeks.org/making-elements-distinct-sorted-array-minimum-increments/
"""
def min_incre(arr):
	gap=[]
	redun=[]
	init_sum=sum(arr)
	for i in range(0, len(arr)):
		if arr[i]==arr[i-1]:
			redun.append(arr[i])
		elif arr[i]-arr[i-1]>1:
			for j in range(arr[i-1]+1, arr[i]):
				gap.append(j)
	

test1=[2, 2, 3, 5, 6]
print min_incre(test1)