def calculate(s: str) -> int:
    # num = 0
    # sign = "+"
    # stack = []
    # for i in range(len(s)):
    #     if s[i].isdigit():
    #         num = num * 10 + int(s[i])
    #     if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
    #         if sign == "+":
    #             stack.append(num)
    #         elif sign == "-":
    #             stack.append(-num)
    #         elif sign == "/":
    #             num = int(stack.pop() / num)
    #             stack.append(num)
    #         elif sign == "*":
    #             num = int(stack.pop() * num)
    #             stack.append(num)
    #         sign = s[i]
    #         num = 0
    # return sum(stack)stack = []
    stack = []
    sign = "+"
    num = 0
    for i, c in enumerate(s):
        if c.isdigit():
            num = num * 10 + int(c)
        if (not c.isdigit() and not c.isspace()) or i == len(s) - 1:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                stack.append(stack.pop() // num)
            sign = c
            num = 0
    return sum(stack)
    # stack, num, sign = [], 0, "+"
    # for i in range(len(s)):
    #     if s[i].isdigit():
    #         num = num * 10 + ord(s[i]) - ord("0")
    #     if (not s[i].isdigit() and not s[i].isspace()) or i == len(s) - 1:
    #         if sign == "-":
    #             stack.append(-num)
    #         elif sign == "+":
    #             stack.append(num)
    #         elif sign == "*":
    #             stack.append(stack.pop() * num)
    #         else:
    #             tmp = stack.pop()
    #             if tmp // num < 0 and tmp % num != 0:
    #                 stack.append(tmp // num + 1)
    #             else:
    #                 stack.append(tmp // num)
    #         sign = s[i]
    #         num = 0
    # return sum(stack)


# print(calculate("3+2*2"))
# print(calculate(" 3/2 "))
print(calculate("42"))
print(calculate("14-3/2"))
