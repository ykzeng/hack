def subarraySum(self, nums: List[int], k: int) -> int:
    ans = 0
    prefix = 0
    d = {0: 1}
    for n in nums:
        prefix += n
        if prefix - k in d:
            ans += d[prefix - k]
        d[prefix] = d.get(prefix, 0) + 1
    return ans
