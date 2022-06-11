class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans, n, carry = 0, len(digits), 1
        for i in range(n):
            hi = n - 1 - i
            cur = carry + digits[hi]
            if cur < 10:
                digits[hi] = cur
                carry = 0
            else:
                digits[hi] = 0
                carry = 1
        return digits if carry == 0 else [1] + digits
