"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        node = Node(val=insertVal)
        if not head:
            node.next = node
            return node
        prev, cur = head, head.next
        while prev.next != head:
            if cur.val >= insertVal >= prev.val:
                break
            elif prev.val > cur.val and (insertVal < cur.val or insertVal > prev.val):
                break
            prev, cur = prev.next, cur.next
        node.next, prev.next = cur, node
        return head
