"""
OA
find the first unique character in a string
"""
def test(s):
    occ={}
    for i in range(0, len(s)):
        if s[i] in occ:
            occ[s[i]]+=1
        else:
            occ[s[i]]=1
    for i in range(0, len(s)):
        if occ[s[i]]==1:
            return i
    return -1

def findFirstUniqueChar(s):
    count = {}
    for c in s:
        if c in count:
            count[c] = count[c] + 1
        else:
            count[c] = 1
    for c in s:
        if count[c]==1:
            return c

s = "this is my best act and coding script"
print(findFirstUniqueChar(s))

test1="leetcode"
print test(test1)

test2="love leetcode"
print test(test2)

test3="cc"
print test(test3)