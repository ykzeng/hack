class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnt = collections.Counter(s)
        res = 0
        for k, c in cnt.items():
            if c % 2 != 0:
                res += 1
        return res <= 1
