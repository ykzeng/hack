class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, cur = [], ''
        for c in s:
            if c == '(':
                stack += [cur]
                cur = ''
            elif c == ')':
                if stack:
                    cur = stack.pop() + '(' + cur + ')'
            else:
                cur += c

        while(stack):
            cur = stack.pop() + cur
        return cur
        # from collections import deque
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
samples = ["lee((t)code", "lee((t)c)o(de)", "lee(t(c)o)de)",
           "a)b(c)d", "))((", "(a(b(c)d)"]
for sa in samples:
    print("input string:\t"+str(sa))
    print("output:\t"+str(s.minRemoveToMakeValid(sa)))
