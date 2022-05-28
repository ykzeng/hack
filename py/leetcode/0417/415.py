class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def to_int(n):
            return ord(n) - ord("0")

        carry = i = 0
        l1, l2 = len(num1), len(num2)
        m = max(l1, l2)
        num1, num2 = num1[::-1].ljust(m, "0"), num2[::-1].ljust(m, "0")
        ans = ""
        while i < m:
            n1, n2 = to_int(num1[i]), to_int(num2[i])
            s = n1 + n2 + carry
            ans += str(s % 10)
            carry = s // 10
            i += 1
        return (ans + str(carry))[::-1] if carry > 0 else ans[::-1]
