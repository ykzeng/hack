def minRemoveToMakeValid(self, s: str) -> str:
    lst = list(s)
    stack = []
    res = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                c = ""
        res.append(c)
    for i in stack:
        res[i] = ""
    return "".join(res)
