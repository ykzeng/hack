# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.bsearch(root, val)

    def bsearch(self, node, val):
        if not node:
            return None
        if node.val == val:
            return node
        elif node.val < val:
            return self.bsearch(node.right, val)
        else:
            return self.bsearch(node.left, val)
