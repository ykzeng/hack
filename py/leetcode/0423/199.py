class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = {}

        def porder(node, depth):
            if not node:
                return
            if depth not in ans:
                ans[depth] = node.val
            porder(node.right, depth + 1)
            porder(node.left, depth + 1)

        porder(root, 0)
        return ans.values()
