class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quadratic(x):
            return a*x*x+b*x+c
        if a==0:
            ans=[quadratic(n) for n in nums]
            return ans if b>=0 else ans[::-1]
        vertex=-b/(2*a)
        lo,hi=0,len(nums)-1
        # assuming a>0
        ans=[]
        while(lo<=hi):
            diff_lo=abs(nums[lo]-vertex)
            diff_hi=abs(nums[hi]-vertex)
            if diff_lo>=diff_hi:
                ans.append(quadratic(nums[lo]))
                lo+=1
            else:
                ans.append(quadratic(nums[hi]))
                hi-=1
        return ans[::-1] if a>0 else ans