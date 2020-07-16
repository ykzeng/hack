from typing import List


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # FINAL
        if not s:
            return False

        ss = (s + s)[1:-1]
        return ss.find(s) != -1
        # SOLUTION 3 - very slow ~20%
        # n = len(s)
        # rep = s+s
        # rep = rep[1:]
        # for i in range(0, n-1):
        #     if rep[i:i+n] == s:
        #         return True
        # return False
        # SOLUTION 2 - ~60%
        # for i in range(1, int(len(s)/2)+1):
        #     flag = True
        #     if (len(s) % i) != 0:
        #         continue
        #     for j in range(1, int(len(s)/i)):
        #         if s[0:i] != s[j*i:j*i+i]:
        #             flag = False
        #             break
        #     if flag:
        #         return flag
        # return False
        # SOLUTION 1
        # try to use equal sequence to solve problem
        # failed because sometimes in a repeated substring list
        # there might be chars with inequal sequence
        # abacd, abacd, abacd
        # a-a: 2, 3
        # b/c/d-b/c/d: 5
        # recur = [0]*26
        # last = [-1]*26
        # for i in range(0, len(s)):
        #     c = s[i]
        #     if recur[c-'a'] == 0 and last[c-'a'] == -1:
        #         last[c-'a'] = i
        #     elif recur[c-'a'] == 0:
        #         recur[c-'a'] = i - last[c-'a']
        #     elif recur[c-'a'] != i - last[c-'a']:
        #         return False


s = Solution()
print(s.repeatedSubstringPattern("abab"))
print(s.repeatedSubstringPattern("aba"))
print(s.repeatedSubstringPattern("abcabcabcabc"))
