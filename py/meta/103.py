# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # q,ans = [(root,0)],collections.defaultdict(list)
        # for node,depth in q:
        #     if not node: continue
        #     ans[depth].append(node.val)
        #     q.append((node.left,depth+1))
        #     q.append((node.right,depth+1))
        # for k in ans:
        #     if k%2!=0: ans[k] = ans[k][::-1]
        # return ans.values()
        if not root:
            return []
        q = deque([root])
        ans, direction = [], 1
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if direction == -1:
                level = level[::-1]
            ans.append(level)
            direction *= -1
        return ans
