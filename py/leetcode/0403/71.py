def simplifyPath(path: str) -> str:
    ans = []
    for fdir in path.split("/"):
        if fdir == "..":
            if len(ans) > 0:
                ans.pop()
        elif fdir and fdir != ".":
            ans.append(fdir)
    return "/" + "/".join(ans)


print(simplifyPath("/../"))
