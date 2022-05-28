def minAddToMakeValid(s: str) -> int:
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")" and stack and stack[-1] == "(":
            stack.pop()
        elif c == ")":
            stack.append(c)
    return len(stack)


print(minAddToMakeValid("()))(("))
