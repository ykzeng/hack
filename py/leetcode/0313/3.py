def lengthOfLongestSubstring(self, s: str) -> int:
    start = 0
    res = 0
    exist = {}
    for i, c in enumerate(s):
        if c in exist and start <= exist[c]:
            start = exist[c] + 1
        else:
            res = max(res, i - start + 1)
        exist[c] = i
    return res
    # i = 0
    # res = 0
    # while i < (len(s) - 1):
    #     exist = set(s[i])
    #     for j in range(i + 1, len(s)):
    #         if s[j] in exist:
    #             l = j - i
    #             res = l if l > res else res
    #             i = j
    #             break
    #         else:
    #             exist.add(s[j])
    # return res


print(lengthOfLongestSubstring("abcabcbb"))
