from typing import List
from collections import deque
"""
    do bfs, put all the nodes into an array in the right bfs sequece
"""


def simple_bfs(n, arr):
    arr.append(n.val)
    if n.left:
        simple_bfs(n.left, arr)
    if n.right:
        simple_bfs(n.right, arr)
    return arr


def bfs(root):
    q = deque()
    q.append(root)
    visited = []
    while(q):
        n = q.popleft()
        visited.append(n.val)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    return visited


def dfs(root):
    q = deque()
    q.append(root)
    visited = []
    while(q):
        n = q.pop()
        visited.append(n.val)
        # post order traversal
        if n.right:
            q.append(n.right)
        if n.left:
            q.append(n.left)
    return visited

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # v3 - leetcode discussion
        info = []

        def dfs(node, depth=0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)

        return [s/float(c) for s, c in info]
    # v2 - pure dfs
    # def dfs(node, depth, d):
    #     if depth in d:
    #         d[depth].append(node.val)
    #     else:
    #         d[depth] = [node.val]
    #     if node.left:
    #         dfs(node.left, depth+1, d)
    #     if node.right:
    #         dfs(node.right, depth+1, d)
    # d = {}
    # dfs(root, 0, d)
    # i = 0
    # res = []
    # while(i in d):
    #     res.append(sum(d[i])/len(d[i]))
    #     i += 1
    # return res
    # v1
    # curLv, nextLv = deque(), deque()
    # res, arr = [], []
    # curLv.append(root)
    # while(curLv or nextLv):
    #     if not curLv:
    #         temp = curLv
    #         curLv = nextLv
    #         nextLv = temp
    #         res.append(sum(arr)/len(arr))
    #         arr = []
    #     else:
    #         n = curLv.popleft()
    #         arr.append(n.val)
    #         if n.left:
    #             nextLv.append(n.left)
    #         if n.right:
    #             nextLv.append(n.right)
    # res.append(sum(arr)/len(arr))
    # return res

    # TEST the simple simple_bfs function
    # s = Solution()
    # tsamples = [TreeNode(3,TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))]
    # for t in tsamples:
    #     print(simple_bfs(t, []))


    # TEST the simple simple_bfs function
s = Solution()
tsamples = [TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))]
for t in tsamples:
    print(bfs(t))

for t in tsamples:
    print(dfs(t))

for t in tsamples:
    print(s.averageOfLevels(t))
