class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def move(x, y):
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    yield nx, ny

        def dfs(x, y, i):
            area = 0
            grid[x][y] = i
            for nx, ny in move(x, y):
                if grid[nx][ny] == 1:
                    area += dfs(nx, ny, i)
            return area + 1

        i = 2
        area = {0: 0}
        for x, y in itertools.product(range(n), range(n)):
            if grid[x][y] == 1:
                area[i] = dfs(x, y, i)
                i += 1
        res = max(area.values())
        for x, y in itertools.product(range(n), range(n)):
            if grid[x][y] == 0:
                possible = set(grid[nx][ny] for nx, ny in move(x, y))
                tot_area = sum([area[i] for i in list(possible)])
                res = max(res, sum(area[index] for index in possible) + 1)
        return res
