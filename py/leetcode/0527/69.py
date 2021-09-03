class Solution:
    def mySqrt(self, x: int) -> int:
        lo,hi=0,x
        while lo<hi:
            mid=lo+(hi-lo)//2
            if mid*mid<=x and (mid+1)*(mid+1)>x:
                return mid
            elif mid*mid>x:
                hi=mid-1
            else:
                lo=mid+1
        return lo