class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = [intervals[0]]
        for x in range(1, len(intervals)):
            i = intervals[x]
            if ans[-1][-1] >= i[0]:
                ans[-1][-1] = max(i[1], ans[-1][-1])
            else:
                ans.append(i)
        return ans
