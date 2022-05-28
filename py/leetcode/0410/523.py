class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rolling = 0
        d = {0: -1}
        for i, n in enumerate(nums):
            rolling = (rolling + n) % k
            if rolling not in d:
                d[rolling] = i
            else:
                if i - d[rolling] >= 2:
                    return True
        return False
