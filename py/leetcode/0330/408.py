def validWordAbbreviation(word: str, abbr: str) -> bool:
    i = j = 0
    while i < len(word) and j < len(abbr):
        if word[i] == abbr[j]:
            i, j = i + 1, j + 1
        elif abbr[j] == "0":
            return False
        elif abbr[j].isnumeric():
            k = j
            while k < len(abbr) and abbr[k].isnumeric():
                k += 1
            num = int(abbr[j:k])
            i += num
            j = k
        else:
            return False
    return i == len(word) and j == len(abbr)


print(validWordAbbreviation("a", "01"))
