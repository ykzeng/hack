def minAddToMakeValid(self, s: str) -> int:
    lstack, rstack = [], []
    for c in s:
        if c == "(":
            lstack.append(c)
        elif c == ")":
            if lstack:
                lstack.pop()
            else:
                rstack.append(c)
    return len(lstack) + len(rstack)

    # lcnt = rcnt = 0
    # for c in s:
    #     if c=='(':
    #         lcnt += 1
    #     elif c==')':
    #         if lcnt > 0:
    #             lcnt -= 1
    #         else:
    #             rcnt += 1
    # return lcnt+rcnt
