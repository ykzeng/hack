class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = collections.defaultdict(list)
        for x in range(len(mat)):
            for y in range(len(mat[x])):
                d[x + y] += [mat[x][y]]
        ans = []
        for k in d:
            if k % 2 != 0:
                arr = d[k]
            else:
                arr = d[k][::-1]
            ans.extend(arr)
        return ans
