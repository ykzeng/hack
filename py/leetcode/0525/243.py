class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i1,i2=-1,-1
        ans=len(wordsDict)
        for i,w in enumerate(wordsDict):
            if w==word1:
                i1=i
            if w==word2:
                i2=i
            if i1!=-1 and i2!=-1:
                ans=min(ans,abs(i1-i2))
        return ans