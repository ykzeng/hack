# 953. Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # d = {c: i for i, c in enumerate(order)}
        # orderList = [[d[c] for c in w] for w in words]

        # def compare(ord1, ord2):
        #     i = 0
        #     while i < len(ord1) and i < len(ord2):
        #         if ord1[i] <= ord2[i]:
        #             return True
        #         i += 1
        #     return True
        # for i in range(0, len(words)-1):
        #     if not compare(orderList[i], orderList[i+1]):
        #         return False
        # return True
        # Online SOL - 50%
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))
        # SOL 1 - 80%
        # d = {}
        # for i in range(0, len(order)):
        #     d[order[i]] = i
        # for i in range(0, len(words)-1):
        #     w1 = words[i]
        #     w2 = words[i+1]
        #     for j in range(0, len(w1)):
        #         if j >= len(w2) or d[w1[j]] > d[w2[j]]:
        #             return False
        #         elif d[w1[j]] == d[w2[j]]:
        #             continue
        #         else:
        #             break
        #     if len(w2) >= len(w1):
        #         continue
        # return True


s = Solution()
samples = [(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"), (["fxasxpc", "dfbdrifhp", "nwzgs", "cmwqriv", "ebulyfyve", "miracx", "sxckdwzv", "dtijzluhts", "wwbmnge", "qmjwymmyox"],
                                                                   "zkgwaverfimqxbnctdplsjyohu"),
           (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz"),
           (["apple", "app"], "abcdefghijklmnopqrstuvwxyz")]
for sa in samples:
    print("input string:\t"+str(sa))
    print("output:\t"+str(s.isAlienSorted(sa[0], sa[1])))
    print()

# playing around Online SOL
# words = ["fxasxpc", "dfbdrifhp", "nwzgs", "cmwqriv", "ebulyfyve",
#          "miracx", "sxckdwzv", "dtijzluhts", "wwbmnge", "qmjwymmyox"]
# order = "zkgwaverfimqxbnctdplsjyohu"
# m = {c: i for i, c in enumerate(order)}
# words = [[m[c] for c in w] for w in words]
# print(words)
# print(str(tuple(zip(words, words[1:]))))
# print(str(tuple(w1 <= w2 for w1, w2 in zip(words, words[1:]))))
# return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))
