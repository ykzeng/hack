class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i, j = 0, 0
        while k > 0:
            i += 1
            if j < len(arr) and i == arr[j]:
                j += 1
            else:
                k -= 1
        return i
