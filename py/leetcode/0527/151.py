class Solution:
    def reverseWords(self, s: str) -> str:
        # arr=s.strip().split()
        # return ' '.join(arr[::-1])
        # stack=[]
        # cur=''
        # for c in (s+' '):
        #     if c==' ':
        #         if cur!='':
        #             stack.append(cur)
        #             cur=''
        #     else:
        #         cur+=c
        # ans=''
        # for i in range(len(stack)-1,-1,-1):
        #     ans+=stack[i]+' '
        # return ans[:-1]
        ans=''
        word=''
        for c in s[::-1]:
            if c!=' ':
                word=c+word
            else:
                ans=ans+' '+word
                word=''
        return (ans+' '+word)[1:]