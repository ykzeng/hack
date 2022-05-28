def validWordAbbreviation(word: str, abbr: str) -> bool:
    i = j = 0
    digit = ""
    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit() and abbr[j] == "0":
            return False
        if abbr[j].isdigit():
            while j < len(abbr) and abbr[j].isdigit():
                digit += abbr[j]
                j += 1
            i += int(digit)
            digit = ""
        elif abbr[j] == word[i]:
            i, j = i + 1, j + 1
        else:
            return False
    return i == len(word) and j == len(abbr)


print(validWordAbbreviation("internationalization", "i12iz4n"))
