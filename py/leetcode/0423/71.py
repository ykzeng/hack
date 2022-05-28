class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split("/")
        res = []
        for i in range(len(dirs)):
            if dirs[i] and dirs[i] != ".." and dirs[i] != ".":
                res.append(dirs[i])
            elif dirs[i] == ".." and res:
                res = res[:-1]
        res = "/" + "/".join(res)
        return res
