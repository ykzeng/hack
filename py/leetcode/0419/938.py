# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # q = [root]
        # ans = 0
        # for node in q:
        #     if not node:
        #         continue
        #     if low <= node.val <= high:
        #         ans += node.val
        #     q.append(node.left)
        #     q.append(node.right)
        # return ans
        if not root:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        return (
            self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
            + root.val
        )
