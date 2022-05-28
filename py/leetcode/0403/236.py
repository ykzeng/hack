# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        self.path_list = []
        self.traverse(root, p, q, [])
        # print(self.path_list)
        # print(len(self.path_list[0]))
        # print(len(self.path_list[1]))
        mlen = min(len(self.path_list[0]), len(self.path_list[1]))
        for i in range(mlen):
            if self.path_list[0][i] != self.path_list[1][i]:
                return self.path_list[0][i - 1]
        return self.path_list[0][mlen - 1]

    def traverse(self, node, t1, t2, path):
        if node:
            if node == t1 or node == t2:
                path += [node]
                self.path_list.append(path)
                # print("val list")
                # print(val)
                # self.val_list.append(val)
                if len(self.path_list) == 2:
                    return
            self.traverse(node.left, t1, t2, path + [node])
            self.traverse(node.right, t1, t2, path + [node])


# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if root in (None, p, q):
#             return root
#         left,right=(self.lowestCommonAncestor(child,p,q) for child in (root.left,root.right))
#         return root if left and right else (left or right)
