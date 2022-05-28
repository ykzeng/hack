class Solution:
    def calculate(self, s: str) -> int:
        sign = "+"
        ans = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = ""
                while i < len(s) and s[i].isdigit():
                    num += s[i]
                    i += 1
                if sign in ("+", "-"):
                    ans.append(int(sign + num))
                elif sign == "*":
                    ans.append(int(num) * ans.pop())
                else:
                    ans.append(int(ans.pop() / int(num)))
                continue
            elif s[i] in ("+", "-", "*", "/"):
                sign = s[i]
            i += 1
        return sum(ans)
