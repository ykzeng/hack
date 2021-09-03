class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans=0
        nums.sort()
        for hi in range(len(nums)-1,-1,-1):
            lo,mid=0,hi-1
            while(lo<mid):
                if nums[lo]+nums[mid]>nums[hi]:
                    ans+=(mid-lo)
                    mid-=1
                else:
                    lo+=1
        return ans