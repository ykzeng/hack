from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        all_exp = []
        for i in range(1, len(num)):
            if i == 1 or (i > 1 and num[0] != "0"):
                self.dfs(num[i:], num[:i], target, int(
                    num[:i]), int(num[:i]), all_exp)
        return all_exp

    def dfs(self, residual, cur_exp, target, last, cur, all_exp):
        if len(residual) == 0:
            if target == cur:
                all_exp.append(cur_exp)
            return
        for i in range(1, len(residual)+1):
            next_num = int(residual[:i])
            if i == 1 or (i > 1 and residual[0] != "0"):
                add = self.dfs(residual[i:], cur_exp+'+'+str(next_num),
                               target, next_num, cur+next_num, all_exp)
                minus = self.dfs(residual[i:], cur_exp+'-'+str(next_num),
                                 target, -next_num, cur-next_num, all_exp)
                multiply = self.dfs(residual[i:], cur_exp+'*'+str(next_num),
                                    target, last*next_num, cur-last+last*next_num, all_exp)
        # concat = self.dfs(residual, cur_exp+str(next_num), target, )


s = Solution()
samples = [("105", 5)]
for sa in samples:
    print("input string:\t"+str(sa))
    print("output:\t"+str(s.addOperators(sa[0], sa[1])))
