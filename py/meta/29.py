class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        isPos = (dividend < 0) == (divisor < 0)
        ans, dividend, divisor = 0, abs(dividend), abs(divisor)
        while dividend >= divisor:
            power = 0
            while dividend > divisor << (power + 1):
                power += 1
            ans += 1 << power
            dividend -= divisor << power
        ans = ans if isPos else -ans
        # ???
        return min(2147483647, ans)
