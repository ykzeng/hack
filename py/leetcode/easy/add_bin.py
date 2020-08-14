class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # SOL 2 - 50%
        carry = 0
        res = ''
        a = list(a)
        b = list(b)
        while(carry or a or b):
            left = right = 0
            if a:
                left = a.pop()
            if b:
                right = b.pop()
            s = int(left) + int(right) + carry
            carry = 1 if s >= 2 else 0
            s = s % 2
            res = str(s) + res
        return res
        # SOL 1 - 50%
        # n = max(len(a), len(b))
        # a, b = a.zfill(n+1), b.zfill(n+1)
        # carry = 0
        # res = ''
        # for i in range(n, -1, -1):
        #     s = int(a[i]) + int(b[i]) + carry
        #     if s >= 2:
        #         s = s - 2
        #         carry = 1
        #     else:
        #         carry = 0
        #     res = str(s) + res
        # return str(int(res))


s = Solution()
samples = [("11", "1"), ("1010", "1011")]
for sa in samples:
    print("input string:\t"+str(sa))
    print("output:\t"+str(s.addBinary(sa[0], sa[1])))
