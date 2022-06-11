class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # ans = set()
        # def dfs(nums,path):
        #     if not nums:
        #         ans.add(path)
        #         return
        #     for i in range(len(nums)):
        #         dfs(nums[:i]+nums[i+1:],path+(nums[i],))
        # dfs(nums,())
        # return list(ans)
        ans, cnt = [], Counter(nums)

        def dfs(path, cnt):
            if len(path) == len(nums):
                ans.append(path)
            for k in cnt:
                if cnt[k] > 0:
                    cnt[k] -= 1
                    dfs(path + [k], cnt)
                    cnt[k] += 1

        dfs([], cnt)
        return ans
