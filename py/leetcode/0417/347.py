def topKFrequent(nums, k: int):
    bucket = [[] for i in range(len(nums) + 1)]
    from collections import Counter
    from itertools import chain

    cnt = Counter(nums)
    for n in cnt:
        occurence = cnt[n]
        # print(occurence)
        # print(len(bucket))
        bucket[occurence].append(n)
    return list(chain(*bucket))[::-1][:k]


print(topKFrequent([1], 1))
