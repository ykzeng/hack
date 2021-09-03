class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=imax=nums[0]
        for n in nums[1:]:
            imax=max(imax+n,n)
            ans=max(imax,ans)
        return ans