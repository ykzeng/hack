class Solution:
    def numberToWords(self, num: int) -> str:
        lt20=["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        lt100=["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        ks=["","Thousand","Million","Billion"]
        def n2w(num):
            if num==0:
                return ""
            if num<20:
                return lt20[num]+" "
            if num<100:
                return lt100[num//10]+" "+n2w(num%10)
            if num<1000:
                return lt20[num//100]+" Hundred "+n2w(num%100)
        if num==0:
            return "Zero"
        k=0
        ans=''
        while(num>0):
            if num%1000!=0:
                ans=n2w(num%1000)+ks[k]+" "+ans
            num=num//1000
            k+=1
        return ans.strip()