# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque()
        for c in s:
            if (len(stack) != 0):
                if(stack[-1] == '(' and c == ')') or (stack[-1] == '[' and c == ']') or (stack[-1] == '{' and c == '}'):
                    stack.pop()
                    continue
            stack.append(c)
        return len(stack) == 0


s = Solution()
samples = ["()", "()[]{}", "(]", "([)]", "{[]}", "(]", "){"]
for sa in samples:
    print("input string:\t"+sa)
    print("output:\t"+str(s.isValid(sa)))
