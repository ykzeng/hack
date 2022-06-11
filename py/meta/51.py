class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def dfs(queens, xydiff, xysum):
            y = len(queens)
            if y == n:
                ans.append(queens)
                return
            for x in range(n):
                if x - y not in xydiff and x + y not in xysum and x not in queens:
                    dfs(queens + [x], xydiff + [x - y], xysum + [x + y])

        dfs([], [], [])
        return [["." * x + "Q" + "." * (n - x - 1) for x in sol] for sol in ans]
