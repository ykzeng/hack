vec1 = [1,2,3,4,5]
vec2 = [-1,0,7,8,10]

def twoSum(arr, k):
    diff = []
    count = {}
    for a in arr:
        diff.append(k - a)
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    numPairs = 0
    for d in diff:
        if d in count:
            numPairs += count[d]
    return int(numPairs / 2)

print(twoSum(vec1, 7))
print(twoSum(vec2, 7))