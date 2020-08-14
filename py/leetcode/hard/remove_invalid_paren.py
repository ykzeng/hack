from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                if c == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        level = {s}
        while True:
            res = []
            for e in level:
                if isValid(e):
                    res.append(e)
            if res:
                return res
            next_lv = set()
            for e in level:
                for i in range(0, len(e)):
                    next_lv.add(e[:i]+e[i+1:])
            level = next_lv


s = Solution()
samples = ["()())()", "(a)())()", ")("]
for sa in samples:
    print("input string:\t"+str(sa))
    print("output:\t"+str(s.removeInvalidParentheses(sa)))
