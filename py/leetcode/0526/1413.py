class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # s+x>=1
        # min(s)+x>=1
        # get min(s)->x=1-min(s)
        s=0
        ans=1
        for n in nums:
            s+=n
            ans=max(ans,1-s)
        return ans