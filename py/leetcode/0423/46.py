class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(nums, path):
            if len(nums) == 1:
                ans.append(path + nums)
                return
            for i in range(len(nums)):
                helper(nums[:i] + nums[i + 1 :], path + [nums[i]])
            return

        helper(nums, [])
        return ans
