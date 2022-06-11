class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def valid(target, k):
            res = 0
            for r in ribbons:
                res += r // target
            return res >= k

        lo, hi = 1, max(ribbons) + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if valid(mid, k):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
