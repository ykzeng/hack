class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = len(x)
        for i in range(0, int(n/2)):
            right = n-i-1
            if x[i] != x[right]:
                return False
        return True


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
