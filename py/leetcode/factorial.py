
# def fac(n):
#     # # how many 5s we have
#     # n/10
#     # # how many 25s we have
#     # n/25*2
#     # # how many 10s we have
#     # n/10
#     # # minus how many dups of [10s and 25s] we have
#     while(m)
#     return n/5+n/25+n/125+n/625
def fac(n):
    count = 0
    while(n > 5):
        n = int(n/5)
        count += n
    return count


# 100/5
n = 1000

print(fac(n))
