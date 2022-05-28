class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random

        pivot = random.choice(nums)
        left = [n for n in nums if n > pivot]
        mid = [n for n in nums if n == pivot]
        right = [n for n in nums if n < pivot]
        L, M = len(left), len(mid)
        if k <= L:
            return self.findKthLargest(left, k)
        elif L + M < k:
            return self.findKthLargest(right, k - L - M)
        else:
            return mid[0]
