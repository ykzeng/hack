class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = collections.defaultdict(list)
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                ans[x + y].append(mat[x][y])
        res = []
        for k in ans:
            if k % 2 == 0:
                res.extend(ans[k][::-1])
            else:
                res.extend(ans[k])
        return res
