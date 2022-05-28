def validPalindrome(self, s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            left, right = s[i:j], s[i + 1 : j + 1]
            return left == left[::-1] or right == right[::-1]
        i += 1
        j -= 1
    return True
