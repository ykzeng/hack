from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        llen = len(nums)
        for i in range(0, (llen-1)):
            res.append(nums[i]*res[i])
        sec = 1
        for i in range((llen-2), -1, -1):
            sec = sec * nums[i+1]
            res[i] = res[i]*sec
        return res

        # tot_prod = 1
        # for n in nums:
        #     tot_prod = tot_prod * n
        # arr = [int(tot_prod/n) for n in nums]
        # return arr
s = Solution()
samples = [[1, 2, 3, 4]]
for sa in samples:
    print("input string:\t"+str(sa))
    print("output:\t"+str(s.productExceptSelf(sa)))
