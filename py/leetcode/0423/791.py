def customSortString(order: str, s: str) -> str:
    import collections

    cnt = collections.Counter(s)
    ans = [cnt.pop(c) * c for c in order if c in cnt]
    for c, v in cnt.items():
        ans.append(v * c)
    return "".join(ans)


print(customSortString("cba", "abcd"))
