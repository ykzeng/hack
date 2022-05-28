def gg(s):
    """Return possible length."""
    # ans = {int(s)}
    # for i in range(1, len(s)):
    #     ans |= {x + y for x in gg(s[:i]) for y in gg(s[i:])}
    # return ans
    ans = {int(s)}
    for i in range(1, len(s)):
        ans |= {x + y for x in gg(s[i:]) for y in gg(s[:i])}
    return ans


print(gg("1233"))
