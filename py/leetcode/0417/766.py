def isToeplitzMatrix(matrix) -> bool:
    m, n = len(matrix), len(matrix[0])
    for x in range(m):
        for y in range(n):
            nx, ny = x + 1, y + 1
            if nx < m and ny < n:
                if matrix[nx][ny] != matrix[x][y]:
                    return False
    return True


isToeplitzMatrix([[11, 74, 0, 93], [40, 11, 74, 7]])
