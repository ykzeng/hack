from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = [0] * (len(nums)+1)
        for n in nums:
            count[n]+=1
        res = [nums[0], nums[1]]
        for i in range(1, len(count)):
            if count[i] > 1:
                res[0] = i
            if count[i] == 0:
                res[1] = i
        return res
s = Solution()
print(s.findErrorNums([1,2,2,4]))