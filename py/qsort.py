
def qsort(arr, lo, hi):
    if lo < hi:
        mid = partition(arr, lo, hi)
        qsort(arr, lo, mid-1)
        qsort(arr, mid+1, hi)
    return arr

def partition(arr, lo, hi):
    piv = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] < piv:
            i+=1
            swap(arr, i, j)
    swap(arr, i+1, hi)
    return (i+1)


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    

samples = [[5,10,20,104,30,-1,0,23,53,-100,-2,0], 
[-1,-4,-7,-10,-0.5,2,5,4,2,60]]
for s in samples:
    print("test case: "+str(s))
    print("sorted: "+str(qsort(s, 0, (len(s)-1))))