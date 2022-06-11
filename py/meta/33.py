class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        rot = lo
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            realmid = (rot + mid) % len(nums)
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
