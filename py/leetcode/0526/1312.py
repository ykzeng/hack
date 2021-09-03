class Solution:
    def minInsertions(self, s: str) -> int:
        dp=[[0 for i in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i]=1
            for j in range(i-1,-1,-1):
                if s[i]==s[j]:
                    dp[i][j]=2+dp[i-1][j+1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j+1])
        return len(s)-dp[len(s)-1][0]