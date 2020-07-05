import math

num = 180*7

def primeFactors(num):
    n = num
    fac = []
    while n % 2 == 0:
        n = n / 2
        fac.append(2)
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            n = int(n / i)
            fac.append(i)
    print("final n:"+str(n))
    print("factors:"+str(fac))
    
    # ???
    # Condition if n is a prime 
    # number greater than 2 
    # if n > 2: 
    #     print n 
    
    return fac

print(primeFactors(num))