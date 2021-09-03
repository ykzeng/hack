class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s=sum(nums)
        if s%k!=0:
            return False
        s=s/k
        visited=[False]*len(nums)
        def canPartition(nums,s,target,k,start):
            # if s==target:
            #     s=0
            #     k-=1
            if k==1:
                return True
            if s==target:
                return canPartition(nums,0,target,k-1,0)
            for i in range(start,len(nums)):
                if not visited[i]:
                    visited[i]=True
                    s_next=s+nums[i]
                    if canPartition(nums,s_next,target,k,i+1):return True
                    visited[i]=False
            return False
        return canPartition(nums,0,s,k,0)