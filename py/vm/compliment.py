"""
Complement number
https://leetcode.com/problems/number-complement/description/
"""
def findComplement(num):
    """
    :type num: int
    :rtype: int
    """
    bits=[]
    while num/2>0:
    	bit=num%2
    	num=num/2
    	bits.append(bit)
    bits.append(num)
    res=0
    for i in range(0, len(bits)):
    	res+=int(not bits[i])*2**i
    return res

print findComplement(65)