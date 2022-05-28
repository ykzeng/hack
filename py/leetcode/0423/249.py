class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strings:
            key = ()
            for i in range(1, len(s)):
                diff = 26 + ord(s[i]) - ord(s[i - 1])
                key += (diff % 26,)
            res[key] += [s]
        return [res[k] for k in res]
