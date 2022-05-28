class Solution:
    def isPalindrome(self, s: str) -> bool:
        lo, hi = 0, len(s) - 1
        while lo <= hi:
            if not s[lo].isalnum():
                lo += 1
                continue
            if not s[hi].isalnum():
                hi -= 1
                continue
            if s[lo].lower() != s[hi].lower():
                return False
            else:
                lo, hi = lo + 1, hi - 1
        return True
