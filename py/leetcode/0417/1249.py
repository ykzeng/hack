class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove_list = []
        for i, c in enumerate(s):
            if c in ["(", ")"]:
                if c == ")" and stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    stack.append((c, i))
        s = list(s)
        for c, i in stack:
            s[i] = ""
        return "".join(s)
