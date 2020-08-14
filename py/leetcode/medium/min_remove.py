# 1249. Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # SOL 1 - 30%
        # stack = deque()
        # for i in range(0, len(s)):
        #     c = s[i]
        #     if len(stack) != 0:
        #         if stack[-1][0] == '(' and c == ')':
        #             stack.pop()
        #             continue
        #     if c == '(' or c == ')':
        #         stack.append((c, i))
        # print(str(stack))
        # res = ''
        # for i in range(0, len(s)):
        #     c = s[i]
        #     if len(stack) == 0:
        #         res += s[i:]
        #         break
        #     if stack[0][1] != i:
        #         res += c
        #     else:
        #         stack.popleft()
        # return res


s = Solution()
samples = ["lee(t(c)o)de)", "a)b(c)d", "))((", "(a(b(c)d)"]
for sa in samples:
    print("input string:\t"+sa)
    print("output:\t"+s.minRemoveToMakeValid(sa))
    print("")
