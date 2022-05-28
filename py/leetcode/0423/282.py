def addOperators(num: str, target: int):
    ans = []
    if not num:
        return ans

    def helper(path, pos, res, to_mult, num, target):
        if pos == len(num):
            if target == res:
                ans.append(path)
            return
        for i in range(pos, len(num)):
            # if i != pos and num[i] == '0': break
            cur = int(num[pos : i + 1])
            if pos == 0:
                helper(path + str(cur), i + 1, res + cur, cur, num, target)
            else:
                helper(
                    path + "*" + str(cur),
                    i + 1,
                    res - to_mult + to_mult * cur,
                    cur,
                    num,
                    target,
                )
                helper(path + "+" + str(cur), i + 1, res + cur, cur, num, target)
                helper(path + "-" + str(cur), i + 1, res - cur, cur, num, target)

    helper("", 0, 0, 0, num, target)
    return ans


addOperators("105", 5)
