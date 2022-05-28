def partition(arr, lo, hi):
    left = lo - 1
    pivot = arr[hi]
    for i in range(lo, hi):
        if arr[i] <= pivot:
            left += 1
            arr[left], arr[i] = arr[i], arr[left]
    arr[left + 1], arr[hi] = arr[hi], arr[left + 1]
    return left + 1


def qsort(arr, lo, hi):
    if len(arr) == 1:
        return
    if lo < hi:
        pi = partition(arr, lo, hi)

        qsort(arr, lo, pi - 1)
        qsort(arr, pi + 1, hi)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
qsort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
