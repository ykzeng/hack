from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # j = 0
        # for i in range(0, len(nums)):
        #     n = nums[i]
        #     if n == 0:
        #         while(nums[j]==0):
        #             if j == len(nums)-1:
        #                 return nums
        #             j+=1
        #         temp = nums[j]
        #         nums[j] = n
        #         nums[i] = temp
        i = j = 0
        while(j < len(nums) and i < len(nums)):
            zero = nums[j]
            nzero = nums[i]
            if j < i:
                nums[i] = zero
                nums[j] = nzero
            if nums[j] != 0:
                j += 1
            if nums[i] == 0 or j >= i:
                i += 1
        return nums


s = Solution()
samples = [[1, 0]]
for sa in samples:
    print("input string:\t"+str(sa))
    print("output:\t"+str(s.moveZeroes(sa)))
