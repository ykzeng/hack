class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo,hi=0,num
        while lo<hi:
            mid=lo+(hi-lo)//2
            p=mid*mid
            if p>num:
                hi=mid-1
            elif p<num:
                lo=mid+1
            else:
                return True
        return lo*lo==num