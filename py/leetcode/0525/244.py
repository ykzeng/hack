class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.d=collections.defaultdict(list)
        for i,w in enumerate(wordsDict):
            self.d[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        l1=self.d[word1]
        l2=self.d[word2]
        if not l1 or not l2:
            return None
        ans=abs(l1[0]-l2[0])
        i=j=0
        while i<len(l1) and j<len(l2):
            diff=l1[i]-l2[j]
            ans=min(ans,abs(diff))
            if diff>0:
                j+=1
            elif diff<0:
                i+=1
            else:
                return 0
        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)