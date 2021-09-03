class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def dfs(nums,path):
            if len(nums)==0:
                ans.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],path+[nums[i]])
        dfs(nums,[])
        return ans