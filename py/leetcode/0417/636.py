class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans, stack = [0] * n, []
        for l in logs:
            fid, event, time = l.split(":")
            fid, time = int(fid), int(time)
            if event == "start":
                stack.append((fid, time))
            else:
                popped = stack.pop()
                elapsed = time - popped[1] + 1
                ans[fid] += elapsed
                if stack:
                    lastfid = stack[-1][0]
                    ans[lastfid] -= elapsed
        return ans
