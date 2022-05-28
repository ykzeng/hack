def isNumber(s: str) -> bool:
    state_trans = [
        {},
        {" ": 1, "sign": 2, "dgt": 3, ".": 4},
        {"dgt": 3, ".": 4},
        {" ": 9, "e": 6, ".": 5, "dgt": 3},
        {"dgt": 5},
        {"dgt": 5, "e": 6, " ": 9},
        {"sign": 7, "dgt": 8},
        {"dgt": 8},
        {"dgt": 8, " ": 9},
        {" ": 9},
    ]
    state = 1
    # 3,5,8,9
    for c in s:
        if c.isdigit():
            c = "dgt"
        if c == "+" or c == "-":
            c = "sign"
        if c == "E" or c == "e":
            c = "e"
        if c not in state_trans[state]:
            return False
        state = state_trans[state][c]
    if state in [3, 5, 8, 9]:
        return True
    return False


print(isNumber("11"))
