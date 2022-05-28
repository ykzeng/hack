class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def isPossible(ribbons, l, k):
            s = 0
            for r in ribbons:
                s += int(r / l)
            return s >= k

        lo, hi = 1, max(ribbons)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if isPossible(ribbons, mid, k):
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
