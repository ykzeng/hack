class Solution:
    def addBinary(self, a: str, b: str) -> str:
        mlen = max(len(a), len(b))
        a, b = a[::-1].ljust(mlen, "0"), b[::-1].ljust(mlen, "0")
        i = carry = 0
        ans = ""
        while i < len(a):
            na, nb = ord(a[i]) - ord("0"), ord(b[i]) - ord("0")
            s = na + nb + carry
            carry = s // 2
            ans += str(s % 2)
            i += 1
        if carry > 0:
            ans = ans + "1"
        return ans[::-1]
