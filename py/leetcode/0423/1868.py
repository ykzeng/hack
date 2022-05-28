class Solution:
    def findRLEArray(
        self, encoded1: List[List[int]], encoded2: List[List[int]]
    ) -> List[List[int]]:
        i = j = f1 = f2 = v1 = v2 = 0
        m, n, ans = len(encoded1), len(encoded2), []
        while i < m and j < n:
            if not f1 and i < m:
                v1, f1 = encoded1[i]
            if not f2 and j < n:
                v2, f2 = encoded2[j]
            cur_min, prod = min(f1, f2), v1 * v2
            if ans and ans[-1][0] == prod:
                ans[-1][1] += cur_min
            else:
                ans.append([prod, cur_min])
            f1 -= cur_min
            f2 -= cur_min
            i += not f1
            j += not f2
        return ans
