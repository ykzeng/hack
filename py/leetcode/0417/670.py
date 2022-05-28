class Solution:
    def maximumSwap(self, num: int) -> int:
        num = [int(n) for n in str(num)]
        maxi = len(num) - 1
        lo = hi = 0
        for i in range(len(num) - 1, -1, -1):
            if num[i] > num[maxi]:
                maxi = i
            elif num[i] < num[maxi]:
                lo = i
                hi = maxi
        num[lo], num[hi] = num[hi], num[lo]
        return "".join([str(n) for n in num])
        # num = [n for n in str(num)]
        # buckets = [-1 for i in range(10)]
        # for i in range(len(num)-1,-1,-1):
        #     n = num[i]
        #     if buckets[int(n)] == -1:
        #         buckets[int(n)]=i
        # for i in range(len(num)):
        #     for j in range(9,-1,-1):
        #         n = num[i]
        #         if j>int(n) and buckets[j]>i:
        #             num[i],num[buckets[j]] = num[buckets[j]],num[i]
        #             return ''.join(num)
        # return ''.join(num)
