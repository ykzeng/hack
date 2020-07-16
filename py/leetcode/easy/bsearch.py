from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums)
        while(lo < hi):
            mid = int((lo+hi)/2)
            if mid < target:
                lo = mid+1
            else:
                hi = mid
        print(lo)
        if nums[lo] == target:
            return lo
        else:
            return -1


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))
print(s.search([-1, 0, 3, 5, 10, 12], 9))
print(s.search([-1, 0, 3, 5, 9, 12], 2))
