# def findKthLargest(nums, k: int) -> int:
#     def partition(arr, lo, hi):
#         pi = arr[hi]
#         l = lo
#         for r in range(lo, hi):
#             if arr[r] >= pi:
#                 arr[r], arr[l] = arr[l], arr[r]
#                 l += 1
#         arr[l], arr[hi] = arr[hi], arr[l]
#         return l

#     def qsort(arr, lo, hi):
#         if lo < hi:
#             pi = partition(arr, lo, hi)
#             if pi == k - 1:
#                 return
#             elif pi < k - 1:
#                 qsort(arr, pi + 1, hi)
#             else:
#                 qsort(arr, lo, pi - 1)

#     qsort(nums, 0, len(nums) - 1)
#     return nums[k - 1]
import random


def findKthLargest(nums, k):
    if not nums:
        return
    pivot = random.choice(nums)
    left = [x for x in nums if x > pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x < pivot]

    L, M = len(left), len(mid)

    if k <= L:
        return findKthLargest(left, k)
    elif k > L + M:
        return findKthLargest(right, k - L - M)
    else:
        return mid[0]


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
