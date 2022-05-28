class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        visited = set()
        move = [
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1),
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
        ]
        # def dfs(x,y,m,n,path):
        #     if x==m-1 and y==n-1 and grid[x][y]==0:
        #         return len(path)+1
        #     if m>x>=0 and n>y>=0 and grid[x][y]==0 and not visited[x][y]:
        #         visited[x][y] = True
        #         for dx,dy in move:
        #             dfs(x+dx,y+dy,m,n,path+[(x,y)])
        # dfs(0,0,m,n,[])
        # return -1
        q = deque([(0, 0, 1)]) if grid[0][0] == 0 else deque()
        while q:
            x, y, dist = q.popleft()
            if x == m - 1 and y == m - 1 and grid[x][y] == 0:
                return dist
            if m > x >= 0 and m > y >= 0 and grid[x][y] == 0 and (x, y) not in visited:
                visited.add((x, y))
                for dx, dy in move:
                    q.append((x + dx, y + dy, dist + 1))
        return -1
