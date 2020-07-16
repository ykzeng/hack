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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # p = l1
        # q = l2
        # while(p and q):
        #     if p.val >= q.val:
        #         nq = q.next
        #         # frontInsert(p, q)
        #         q.next =
        #         q = nq
        #     elif p.val < q.val:
        #         if p.next == None or q.val <= p.next.val:
        #             np = p.next
        #             nq = q.next
        #             # backInsert(p, q)
        #             p = np
        #             q = nq
        # return p
        p = l1
        q = l2
        res = ListNode(None)
        r = res
        while(p and q):
            # while(True):
            # FIXME this one line will cause bad performance
            # merged it with the while condition
            # if p == None or q == None:
            #     break
            if p.val >= q.val:
                r.next = q
                q = q.next
                r = r.next
            else:
                r.next = p
                p = p.next
                r = r.next
        r.next = p if p != None else q
        return res.next


l1 = ListNode(1, ListNode(2, ListNode(4, None)))
l2 = ListNode(1, ListNode(3, ListNode(4, None)))
print(l1)
print(l2)
s = Solution()
print(s.mergeTwoLists(l1, l2))
