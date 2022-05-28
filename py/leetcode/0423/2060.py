class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        def possible(s):
            ans = {int(s)}
            for i in range(1, len(s)):
                ans |= {x + y for x in possible(s[i:]) for y in possible(s[:i])}
            return ans

        @cache
        def equals(i, j, diff):
            if i == len(s1) and j == len(s2):
                return diff == 0
            if i < len(s1) and s1[i].isdigit():
                hi = i
                while hi < len(s1) and s1[hi].isdigit():
                    hi += 1
                for p in possible(s1[i:hi]):
                    if equals(hi, j, diff - p):
                        return True
            elif j < len(s2) and s2[j].isdigit():
                hi = j
                while hi < len(s2) and s2[hi].isdigit():
                    hi += 1
                for p in possible(s2[j:hi]):
                    if equals(i, hi, diff + p):
                        return True
            elif diff == 0:
                if i < len(s1) and j < len(s2) and s1[i] == s2[j]:
                    return equals(i + 1, j + 1, diff)
            elif diff > 0:
                if i < len(s1):
                    return equals(i + 1, j, diff - 1)
            else:
                if j < len(s2):
                    return equals(i, j + 1, diff + 1)
            return False

        return equals(0, 0, 0)
