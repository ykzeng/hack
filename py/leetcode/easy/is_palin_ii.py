# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/submissions/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while(i < j):
            if s[i] != s[j]:
                return s[i:j] == s[i:j][::-1] or s[i+1:j+1] == s[i+1:j+1][::-1]
            i += 1
            j -= 1
        return True


s = Solution()
samples = ["abca"]
for sa in samples:
    print("input string:\t"+sa)
    print("output:\t"+str(s.validPalindrome(sa)))
