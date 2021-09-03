# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         pA,pB=headA,headB
#         while True:
#             if pA.val==pB.val:
#                 return pA
#             pA=pA.next if pA.next else headA
#             pB=pB.next if pB.next else headB
        a,b=[],[]
        pA,pB=headA,headB
        while pA:
            a=[pA]+a
            pA=pA.next
        while pB:
            b=[pB]+b
            pB=pB.next
        ans=None
        for i in range(min(len(b),len(a))):
            if a[i] is not b[i]:
                return a[i-1] if i-1>=0 else None
        return a[-1] if len(a)<=len(b) else b[-1]