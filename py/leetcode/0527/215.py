class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # def partition(nums,lo,hi):
        #     pi=hi
        #     p=nums[pi]
        #     l=lo
        #     for r in range(lo,hi+1):
        #         if nums[r]>=p:
        #             nums[l],nums[r]=nums[r],nums[l]
        #             l+=1
        #     return l-1
        # def topk(nums,k):
        #     lo,hi=0,len(nums)-1
        #     while lo<hi:
        #         p=partition(nums,lo,hi)
        #         if p==k-1:
        #             return nums[p]
        #         elif p>k-1:
        #             hi=p-1
        #         else:
        #             lo=p+1
        #     return nums[lo]
        # random.shuffle(nums)
        # return topk(nums,k)
        def topk(nums,k):
            p=random.choice(nums)
            l=[n for n in nums if n>p]
            m=[n for n in nums if n==p]
            s=[n for n in nums if n<p]
            L,M=len(l),len(m)
            if L>=k:
                return topk(l,k)
            if L<k and L+M>=k:
                return m[0]
            if L+M<k:
                return topk(s,k-L-M)
        return topk(nums,k)