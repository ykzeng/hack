# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.mindiff = float("inf")
        self.minval = None

        def dfs(node, target):
            if not node:
                return
            diff = abs(node.val - target)
            if diff < self.mindiff:
                self.mindiff = diff
                self.minval = node.val
            dfs(node.left, target)
            dfs(node.right, target)

        dfs(root, target)
        return self.minval
