class Solution:

    def __init__(self, w: List[int]):
        self.cum=[]
        self.s=sum(w)
        cur=0
        for i in w:
            cur+=i/self.s
            self.cum.append(cur)
        self.w=w

    def pickIndex(self) -> int:
        lo,hi=0,len(self.w)-1
        import random
        target=random.random()
        while(lo<hi):
            mid=lo+(hi-lo)//2
            if target==self.cum[mid]:
                return mid
            if target>self.cum[mid]:
                lo=mid+1
            else:
                hi=mid
        return lo


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()