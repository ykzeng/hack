class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def dfs(nums,path):
            if not nums:
                ans.append(path)
                return
            for i in range(len(nums)):
                if i>0 and nums[i-1]==nums[i]:
                    continue
                dfs(nums[:i]+nums[i+1:],path+[nums[i]])
        dfs(nums,[])
        return ans