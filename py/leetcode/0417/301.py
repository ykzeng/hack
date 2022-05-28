class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def remove(s, ans, istart, jstart, openParen, closeParen):
            opencnt = closecnt = 0
            for i in range(istart, len(s)):
                if s[i] == openParen:
                    opencnt += 1
                if s[i] == closeParen:
                    closecnt += 1
                if closecnt > opencnt:
                    for j in range(jstart, i + 1):
                        if s[j] == closeParen and (
                            j == jstart or s[j - 1] != closeParen
                        ):
                            remove(s[:j] + s[j + 1 :], ans, i, j, openParen, closeParen)
                    return
            reverse = s[::-1]
            if openParen == "(":
                remove(reverse, ans, 0, 0, ")", "(")
            else:
                ans.append(reverse)

        ans = []
        remove(s, ans, 0, 0, "(", ")")
        return ans
