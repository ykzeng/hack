"""
Unique Paths problem
https://leetcode.com/problems/unique-paths/description/
"""

def uniquePaths(m, n):
	"""
	:type m: int
	:type n: int
	:rtype: int
	"""
	path_grid=[([0 for i in range(0, m)]) for i in range(0, n)]

	for i in range(0, m):
		path_grid[0][i]=1 
	for i in range(0, n):
		path_grid[i][0]=1 

	for i in range(1, n):
		for j in range(1, m):
			path_grid[i][j]=path_grid[i-1][j]+path_grid[i][j-1]

	return path_grid[n-1][m-1]

print uniquePaths(3, 2)