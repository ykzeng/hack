class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=imax=imin=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            x=max(imax*n,imin*n,n)
            y=min(imax*n,imin*n,n)
            imax=x
            imin=y
            if imax>ans:
                ans=imax
        return ans