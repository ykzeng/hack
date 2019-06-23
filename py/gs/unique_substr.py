def uniqueSubstr(s, k):
    res = set()
    for i in range(0, len(s)-k+1):
        sub_s = s[i : i+k]
        res.add(sub_s)
    print(res)
    resList = list(res)
    resList.sort()
    print(resList)
    return resList

def uniqueSubstrFast(s, k):
    res = []
    for i in range(0, len(s)-k+1):
        sub_s = s[i : i+k]
        strBsInsert(res, 0, len(res)-1, sub_s)
    return  res

def strArrBs(arr, start, end, s):
    if (start < end):
        mid = int(start + (end - start) / 2)
        if(arr[mid] == s):
            return -1
        elif arr[mid] < s:
            return strArrBs(arr, mid+1, end, s)
        else:
            return strArrBs(arr, start, mid-1, s)
    else:
        if arr[start] == s:
            return -1
        elif arr[start] < s:
            return start+1
        else:
            return start
        
def strBsInsert(arr, start, end, s):
    if len(arr) == 0:
        arr.append(s)
    else:
        index = strArrBs(arr, 0, len(arr)-1, s)
        if index != -1:
            arr.insert(index, s)
    return arr

s = "caaab"
s = "caaabla"
k = 2
print("aa"<"ab")
# print(uniqueSubstr(s, k))
print(uniqueSubstrFast(s, k))
# print(strArrBs([1], 0, 0, 0))