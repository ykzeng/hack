class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) >= len(num1):
            short = num1
            longNum = num2
        else:
            short = num2
            longNum = num1
        step = 0
        l = len(longNum)
        s = len(short)
        res = ['0']
        for i in range(0, l):
            if i >= l - s:
                add = int(longNum[i])+int(short[i-l+s])
                if add >= 10:
                    step = 1
                    mod = add - 10
                    res[-1] = str(int(res[-1])+step)
                else:
                    step = 0
                    mod = add
                res.append(str(mod))
            else:
                res.append(str(longNum[i]))
        if res[0] == '0':
            res = res[1:]
        return ''.join(res)


s = Solution()
print(s.addStrings('123', '23'))
print(s.addStrings('123', '2305'))
print(s.addStrings('123', '2909'))
print(s.addStrings('0', '0'))
print(s.addStrings('584', '18'))
