from typing import Counter


def largestIsland(grid) -> int:
    m, n = len(grid), len(grid[0])
    neig_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    from collections import Counter
    from itertools import product

    island = Counter()
    ans = 0

    def dfs(grid, x, y, i):
        if not (x >= 0 and y >= 0 and x < m and y < n and grid[x][y] == 1):
            return
        island[i] += 1
        grid[x][y] = i
        for dx, dy in neig_list:
            dfs(grid, x + dx, y + dy, i)

    cnt = 2
    for x, y in product(range(m), range(n)):
        if grid[x][y] == 1:
            dfs(grid, x, y, cnt)
            cnt += 1
    for x, y in product(range(m), range(n)):
        if grid[x][y] != 0:
            continue
        neig_island = set()
        for dx, dy in neig_list:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and nx < m and ny < n and grid[nx][ny] != 1:
                neig_island.add(grid[nx][ny])
        ans = max(ans, sum(island[i] for i in neig_island) + 1)
    return ans


print(largestIsland([[1, 0], [0, 1]]))
