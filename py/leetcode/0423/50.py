def myPow(x: float, n: int) -> float:
    if n == 1:
        return x
    if n % 2 != 0:
        return myPow(x, n - 1) * x
    else:
        half = myPow(x, n / 2)
        return half * half


print(myPow(2.0, 10))
