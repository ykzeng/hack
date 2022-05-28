# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [(root, 0, 0)]
        ans = collections.defaultdict(list)
        mincol, maxcol = float("inf"), -float("inf")
        for node, col, row in q:
            if not node:
                continue
            mincol = min(mincol, col)
            maxcol = max(maxcol, col)
            q.append((node.left, col - 1, row + 1))
            q.append((node.right, col + 1, row + 1))
            ans[col].append((row, node.val))
        res = []
        for col in range(mincol, maxcol + 1):
            res.append([v for _, v in sorted(ans[col])])
        return res
