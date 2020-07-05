from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # s = max(nums)
        s = nums[0]
        ts = 0
        for i in range(0, len(nums)):
            ts = nums[i] + ts
            if ts > s:
                s = ts
            if ts <= 0:
                ts = 0
        return s
        # V1: time limit exceeded
        # s = nums[0]
        # for i in range(0, len(nums)):
        #     for j in range(0, len(nums)-i):
        #         ts = sum(nums[j:j+i+1])
        #         if ts > s:
        #             s=ts
        # return s

obj = Solution()
s = obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(s)