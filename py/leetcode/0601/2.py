# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1,p2=l1,l2
        ans=res=ListNode(0)
        carry=0
        while(p1 or p2):
            s=(p1.val if p1 else 0)+(p2.val if p2 else 0)+carry
            cur=s%10
            carry=s//10
            res.next=ListNode(cur)
            res=res.next
            p1=p1.next if p1 else p1
            p2=p2.next if p2 else p2
        if carry>0:res.next=ListNode(carry)
        return ans.next