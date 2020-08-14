from typing import List


class Solution:
    def bsearch(self, nums, lo, hi, target):
        if lo > hi:
            return -1
        mid = int((lo+hi)/2)
        if nums[mid] > target:
            return self.bsearch(nums, lo, mid-1, target)
        elif nums[mid] < target:
            return self.bsearch(nums, mid+1, hi, target)
        else:
            return mid

    def search(self, nums: List[int], target: int) -> int:
        return self.bsearch(nums, 0, (len(nums)-1), target)
        # failed version
        # lo = 0
        # hi = len(nums)
        # while(lo < hi):
        #     mid = int((lo+hi)/2)
        #     if mid < target:
        #         lo = mid+1
        #     else:
        #         hi = mid
        # print(lo)
        # if nums[lo] == target:
        #     return lo
        # else:
        #     return -1


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))
print(s.search([-1, 0, 3, 5, 10, 12], 9))
print(s.search([-1, 0, 3, 5, 9, 12], 2))
print(s.search([5], 5))
