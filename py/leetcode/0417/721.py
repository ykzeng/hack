class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email2accnt = collections.defaultdict(list)
        for i, accnt in enumerate(accounts):
            for j in range(1, len(accnt)):
                email = accnt[j]
                email2accnt[email].append(i)
        visited = [False] * len(accounts)

        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for ni in email2accnt[email]:
                    dfs(ni, emails)

        ans = []
        for i in range(len(accounts)):
            if visited[i]:
                continue
            emails = set()
            dfs(i, emails)
            name = accounts[i][0]
            ans.append([name] + sorted(list(emails)))
        return ans
