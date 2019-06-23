def dotProduct(vec1, vec2):
    if len(vec1)!=len(vec2):
        return None
    res = 0
    for i in range(0, len(vec1)):
        res += vec1[i] * vec2[i]
    return res
    
vec1 = [1,2,3,4,5]
vec2 = [-1,0,2,8,10]

print(dotProduct(vec1, vec2))


a = [1, 1, 4, 4, 4, 4, 7, 7, 7, 7, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
b = [2, 2, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
def compress(vec):
    cur = vec[0]
    count = 1
    
    small_vec = []
    for v in vec[1:len(vec)]:
        if v != cur:
            small_vec.append([cur, count])
            cur = v
            count = 1
        else:
            count += 1
    small_vec.append([cur, count])
    return small_vec

small_a = compress(a)
small_b = compress(b)

def dotProductSmall(vec1, vec2):
    v2index = 0
    v2residual = vec2[v2index][1]
    
    #res = 0
    res = []
    for v in vec1:
        v1value = v[0]
        v1residual = v[1]
        while (v1residual > 0):
            v2value = vec2[v2index][0]
            if v2residual > 0:
                v1residual-=1
                v2residual-=1
                #res += v1value * v2value
                res.append(v1value*v2value)
            elif  v2residual == 0:
                v2index+=1
                v2residual = vec2[v2index][1]
    return res

print(dotProductSmall(small_a, small_b))
                