class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)
        return pts[:k]
        # import heapq
        # q = []
        # for p in points:
        #     dist = -p[0]**2-p[1]**2
        #     if len(q)==k:
        #         heapq.heappushpop(q,(dist,p[0],p[1]))
        #     else:
        #         heapq.heappush(q,(dist,p[0],p[1]))
        # return [[x,y]for (dist,x,y) in q]
        # def partition(arr,lo,hi,dist=lambda x:x[0]**2+x[1]**2):
        #     left=lo
        #     pivot=arr[hi]
        #     for i in range(lo,hi):
        #         if dist(arr[i])<=dist(pivot):
        #             arr[left],arr[i]=arr[i],arr[left]
        #             left+=1
        #     arr[left],arr[hi]=arr[hi],arr[left]
        #     return left
        # def qsort(arr,lo,hi):
        #     if lo<hi:
        #         pi=partition(arr,lo,hi)
        #         if pi==k:
        #             return
        #         elif pi<k:
        #             qsort(arr,pi+1,hi)
        #         else:
        #             qsort(arr,lo,pi-1)
        # qsort(points,0,len(points)-1)
        # return points[:k]
