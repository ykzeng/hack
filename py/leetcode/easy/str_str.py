# https://leetcode.com/problems/implement-strstr/
from typing import List


def preproc(needle):
    m = len(needle)
    next = [0]
    i = 1
    now = 0
    while i < m:
        if needle[now] == needle[i]:
            i += 1
            now += 1
            next.append(now)
        elif now:
            now = next[now-1]
        else:
            next.append(0)
            i += 1

    return next


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # SOL 4 - KMP algo
        if needle == '':
            return 0
        for i in range(len(haystack)):
            flag = True
            for j in range(len(needle)):
                if haystack[i+j] == needle[j]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                return i
        return -1

        # SOLUTION 3 - almost identical with SOL 1 ~90%
        # m = len(needle)
        # n = len(haystack)
        # for i in range(0, n-m+1):
        #     if haystack[i:i+m] == needle:
        #         return i
        # return -1
        # SOLUTION 2 ~38%
        # if needle == '':
        #     return 0
        # m = len(needle)
        # n = len(haystack)
        # if n < m:
        #     return -1
        # d = {}
        # for i in range(0, n-m+1):
        #     s = haystack[i:i+m]
        #     if s not in d:
        #         d[s] = i
        # if needle in d:
        #     return d[needle]
        # else:
        #     return -1
        # SOLUTION 1 ~23%
        # if needle == '':
        #     return 0
        # m = len(needle)
        # n = len(haystack)
        # if n < m:
        #     return -1
        # for i in range(0, n-m+1):
        #     if haystack[i:i+m] == needle:
        #         return i
        # return -1


s = Solution()
print(s.strStr("mississippi", "pi"))
print(s.strStr("hello", "ll"))
print(s.strStr("aaaaa", "bba"))
print(s.strStr("aaaaa", ""))
print(preproc('abaabac'))
