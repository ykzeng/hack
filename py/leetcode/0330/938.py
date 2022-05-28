def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    queue = [root]
    res = 0
    for node in queue:
        if node:
            if node.val < low:
                queue += (node.right,)
            elif node.val > high:
                queue += (node.left,)
            # node.val>=low and node.val<=high
            else:
                res += node.val
                queue += node.left, node.right
    return res
