# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        p = self
        s = ''
        while(p):
            s += str(p.val)+'->'
            p = p.next
        return s[:len(s)-2]


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev_val = head.val
        prev = head
        cur = head.next
        while(cur):
            if cur.val == prev_val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev_val = cur.val
                cur = cur.next
                prev = prev.next
        return head


l1 = ListNode(1, ListNode(1, ListNode(2, None)))
l2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None)))))

print(l1)
print(l2)

s = Solution()
print(s.deleteDuplicates(l1))
print(s.deleteDuplicates(l2))
