class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pairs = set([("0", "0"), ("1", "1"), ("8", "8"), ("6", "9"), ("9", "6")])
        lo, hi = 0, len(num) - 1
        while lo <= hi:
            if (num[lo], num[hi]) not in pairs:
                return False
            lo, hi = lo + 1, hi - 1
        return True
