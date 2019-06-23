class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        all_char_count = 26
        start=ord('a')
        charMap1 = [0 for i in range(0, all_char_count)]
        for c in s:
            charMap1[ord(c)-start]+=1
        for c in t:
            charMap1[ord(c)-start]-=1
        for i in charMap1:
            if i != 0:
                return False
        return True