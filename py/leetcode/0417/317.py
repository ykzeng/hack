def shortestDistance(grid) -> int:
    m, n = len(grid), len(grid[0])
    dist = [[0 for _ in range(n)] for _ in range(m)]
    reachable = [[0 for _ in range(n)] for _ in range(m)]
    # def bfs(x,y,dist,reachable,visited):
    #     # if =2, or if =1
    #     move=[[1,0],[0,1],[-1,0],[0,-1]]
    #     for dx,dy in move:
    #         nx,ny=x+dx,y+dy
    #         if 0<=nx<m and 0<=ny<n:
    #             bfs(nx,ny,dist,reachable)
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    bldg = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                bldg += 1
                visited = [[False for _ in range(n)] for _ in range(m)]
                q = [(i, j, 0)]
                for x, y, d in q:
                    for dx, dy in move:
                        nx, ny = x + dx, y + dy
                        if (
                            m > nx >= 0
                            and n > ny >= 0
                            and grid[nx][ny] == 0
                            and not visited[nx][ny]
                        ):
                            q.append((nx, ny, d + 1))
                            dist[nx][ny] += d + 1
                            reachable[nx][ny] += 1
                            visited[nx][ny] = True
    ans = float("inf")
    for i in range(m):
        for j in range(n):
            if reachable[i][j] >= bldg and grid[i][j] == 0:
                ans = min(dist[i][j], ans)
    return ans if ans < float("inf") else -1


print(shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]))
