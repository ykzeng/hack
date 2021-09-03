class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap=[]
        for p in points:
            dist=p[0]*p[0]+p[1]*p[1]
            if len(heap)<k:
                heapq.heappush(heap,(-dist,p[0],p[1]))
            else:
                heapq.heappushpop(heap,(-dist,p[0],p[1]))
        return [[x,y] for (d,x,y) in heap]