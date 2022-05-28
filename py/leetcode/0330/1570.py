class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {}
        for i, n in enumerate(nums):
            if n != 0:
                self.d[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        d1 = self.d
        d2 = vec.d
        res = 0
        for k in d1:
            if k in d2:
                res += d1[k] * d2[k]
        return res
