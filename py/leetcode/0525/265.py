class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        for i in range(1,len(costs)):
            c=costs[i]
            for j in range(len(c)):
                c[j]=min(costs[i-1][:j]+costs[i-1][j+1:])+c[j]
        return min(costs[len(costs)-1])