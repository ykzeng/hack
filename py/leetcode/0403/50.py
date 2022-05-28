def myPow(x: float, n: int) -> float:
    def pow(x, n):
        if n in (0, 1, 2):
            return x**n
        if n % 2 == 0:
            part = myPow(x, n / 2)
            return part * part
        else:
            part = myPow(x, (n - 1) / 2)
            return part * part * x

    if n < 0:
        return 1 / pow(x, -n)
    else:
        return pow(x, n)


print(myPow(2, 10))
