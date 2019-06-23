s = "+4193 with words"
# s = "   -42"
# s = "words and 987"
s = "-91283472332"

def myAtoi(str: str) -> int:
    str=str.strip()
    if len(str)==0:
        return 0
    startIndex = 0
    number = '0'
    if str[0]=='+' or str[0]=='-':
        startIndex = 1
        number=str[0]+number
    for i in range(startIndex, len(str)):
        c = str[i]
        nc = ord(c)
        if nc >= 48 and nc <= 57:
            number += c
        else:
            break
    res = int(number)
    if res < -2**31:
        return -2**31
    elif res > (2**31-1):
        return (2**31-1)
    else:
        return res

print(myAtoi(s))