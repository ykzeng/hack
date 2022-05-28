class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # n = len(grid)
        # if grid[0][0] or grid[n-1][n-1]:
        #     return -1
        # dirs = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1,1], [1,-1], [-1,1]]
        # seen = set()
        # queue = collections.deque([(0,0,1)]) # indice, dist
        # seen.add((0,0))
        # while queue:
        #     i,j,dist = queue.popleft()
        #     if i == n -1 and j == n - 1:
        #         return dist
        #     for d1, d2 in dirs:
        #         x, y = i + d1, j + d2
        #         if 0 <= x < n and 0 <= y < n:
        #             if (x,y) not in seen and grid[x][y] == 0:
        #                 seen.add((x, y))
        #                 queue.append((x, y, dist + 1))
        # return -1
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        action = [(-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
        from collections import deque

        q = deque([(0, 0, 1)])
        seen = set((0, 0))
        while q:
            x, y, d = q.popleft()
            if x == n - 1 and y == n - 1:
                return d
            for a in action:
                x_next = x + a[0]
                y_next = y + a[1]
                if 0 <= x_next < n and 0 <= y_next < n:
                    if (x_next, y_next) not in seen and grid[x_next][y_next] == 0:
                        seen.add((x_next, y_next))
                        q.append((x_next, y_next, d + 1))
        return -1
