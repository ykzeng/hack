# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# takeaways: maybe lambda incurs the hidden cost of capturing all local variables into a closure context, whereas an itemgetter instance does not
# https://stackoverflow.com/questions/17243620/operator-itemgetter-or-lambda/17243726#17243726
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # SOL 4 with hand tuned heapq - 80%
        h = []
        import heapq as hq

        def dist(p):
            return -p[0]*p[0]-p[1]*p[1]
        for p in points:
            d = dist(p)
            if len(h) < K:
                hq.heappush(h, (dist(p), p))
            elif len(h) == K and h[0][0] < d:
                hq.heappush(h, (d, p))
                hq.heappop(h)
        return [p[1] for p in h]
        # SOL 3 with heapq - 80%
        # return heapq.nsmallest(K, points, key=lambda p: p[0]*p[0]+p[1]*p[1])
        # SOL 2 with sorting - 90%
        # from operator import itemgetter
        # pdist = [(p, p[0]*p[0]+p[1]*p[1]) for p in points]
        # pdist.sort(key=itemgetter(1))
        # return [pdist[i][0] for i in range(0, K)]
        # SOL 1 with PQ - 30%
        # from queue import PriorityQueue as pq
        # q = pq()
        # for p in points:
        #     dist = p[0]*p[0] + p[1]*p[1]
        #     q.put((dist, p))
        # res = []
        # while(K>0):
        #     res.append(q.get()[1])
        #     K -= 1
        # return res


s = Solution()
samples = [([[1, 3], [-2, 2]], 1), ([[3, 3], [5, -1], [-2, 4]], 2)]
for sa in samples:
    print("input string:\t"+str(sa))
    print("output:\t"+str(s.kClosest(sa[0], sa[1])))
