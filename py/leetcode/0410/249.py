class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def encode(s):
            # diff = ord(s[0])-ord('a')
            # return ''.join([chr(ord(c)-diff) for c in s])
            if len(s) == 0:
                return -1
            elif len(s) == 1:
                return 1
            res = [0] * (len(s) - 1)
            for i in range(1, len(s)):
                res[i - 1] = (ord(s[i]) - ord(s[i - 1])) % 26
            return tuple(res)

        d = {}
        for s in strings:
            encoded = encode(s)
            d[encoded] = d.get(encoded, [])
            d[encoded].append(s)
        return list(d.values())

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        diff = lambda c1, c2: (ord(c2) - ord(c1) + 26) % 26
        for s in strings:
            circular_key = tuple(diff(c, s[i + 1]) for i, c in enumerate(s[:-1]))
            d[circular_key] += [s]
        return d.values()
