class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for x in range(len(matrix) - 1):
            for y in range(len(matrix[0]) - 1):
                if matrix[x][y] != matrix[x + 1][y + 1]:
                    return False
        return True
