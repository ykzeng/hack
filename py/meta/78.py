class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(nums, path):
            ans.append(path)
            for i in range(len(nums)):
                dfs(nums[i + 1 :], path + [nums[i]])

        dfs(nums, [])
        return ans
