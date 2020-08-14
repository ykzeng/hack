# def qsort(arr, lo, hi):
#     piv = arr[-1]
#     # put all elements smaller than piv in front of it
#     j = 0
#     small = []
#     large = []
#     for i in range(0, len(arr)):
#         e = arr[i]
#         if e < piv:
#             small.append(e)
#         else:
#             large.append(e)
#     res = small + [piv] + large
#     qsort(small, )
#     qsort(large)


def partition(arr, lo, hi):
    piv = arr[hi-1]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= piv:
            i += 1
            swap(arr, i, j)
    return i


def qsort(arr, lo, hi):
    if lo < hi:
        mid = partition(arr, lo, hi)
        qsort(arr, lo, mid)
        qsort(arr, mid+1, hi)
    return arr


def swap(arr, i1, i2):
    temp = arr[i2]
    arr[i2] = arr[i1]
    arr[i1] = temp


sample = [9, 1, 5, -4, 19, -1]

print(partition(sample, 0, len(sample)))

print(qsort(sample, 0, len(sample)))
