def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    return helper(s, wordDict, {})


def helper(s, wordDict, memo):
    if s in memo:
        return memo[s]
    if not s:
        return []

    res = []
    for word in wordDict:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(word)
        else:
            resultOfTheRest = helper(s[len(word) :], wordDict, memo)
            for item in resultOfTheRest:
                item = word + " " + item
                res.append(item)
    memo[s] = res
    return res


wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
