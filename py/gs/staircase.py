def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    method=[]
    for i in range(0, n+1):
        if i<=2:
            method.append(i)
        else:
            method.append(method[i-1]+method[i-2])
    return method[n]

#print climbStairs(2)

# too slow
#def test(s):
#    exist={}
#    for i in range(0, len(s)):
#        char=s[i]
#        flag=True
#        for j in range(i+1, len(s)):
#            if char==s[j]:
#                flag=False
#        if char not in exist and flag:
#            return i
#        exist[char]=True
#    return -1