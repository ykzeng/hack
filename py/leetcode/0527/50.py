class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        minus=True if n<0 else False
        n=abs(n)
        if n==1 or n==0:
            ans=x**n
        elif n%2!=0:
            n-=1
            sub=self.myPow(x,n/2)
            ans*=x*sub*sub
        else:
            sub=self.myPow(x,n/2)
            ans*=sub*sub
        return 1/ans if minus else ans