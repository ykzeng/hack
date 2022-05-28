# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = [(root, 0)]
        ans = collections.defaultdict(list)
        for node, col in q:
            if node:
                ans[col].append(node.val)
                q.append((node.left, col - 1))
                q.append((node.right, col + 1))
        return [ans[k] for k in sorted(ans.keys())]
