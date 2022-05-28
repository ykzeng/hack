class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            else:
                i -= 1
        if i < 0:
            reverse(nums, 0, len(nums) - 1)
        else:
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    break
            nums[j], nums[i] = nums[i], nums[j]
            reverse(nums, i + 1, len(nums) - 1)
        return nums
