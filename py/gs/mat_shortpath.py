"""
OA and leetcode 64
short_r2r_path(OA): find the shortest path from topest row to bottommost row
only permit down-left/down-middle/down-right walk
min_path_sum(leetcode): find shortest path from certain cell to another
only permit down/right walk
"""
import sys

def main():
  #mat=[[1, 2, 3]
  #    [4, 5, 6]
  #    [7, 8, 9]]
  #dist=short_r2r_path(mat)
  #print dist

  # leetcode #64
  grid=[
    [1,3,1],
    [1,5,1],
    [4,2,1]
  ]
  min_path_sum(grid, 2, 2)

# we suppose the starting point at left-up corner
def min_path_sum(grid, dest_x, dest_y):
  final_grid=[ [-1]*len(grid[0]) for _ in xrange(len(grid)) ]
  final_grid[0][0]=grid[0][0]
  for i in range(1, len(grid[0])):
    final_grid[0][i]=final_grid[0][i-1]+grid[0][i]
  for i in range(1, len(grid)):
    final_grid[i][0]=final_grid[i-1][0]+grid[i][0]
  print final_grid
  min_path=back_track(grid, final_grid, dest_x, dest_y)
  print final_grid
  print min_path
  
def back_track(init_grid, grid, dest_x, dest_y):
  if grid[dest_x][dest_y]==-1:
    left=back_track(init_grid, grid, dest_x-1, dest_y)
    up=back_track(init_grid, grid, dest_x, dest_y-1)
    grid[dest_x][dest_y]=init_grid[dest_x][dest_y]+min(left, up)
  return grid[dest_x][dest_y]


# suppose we only care about row to row shortest distance
def short_r2r_path(mat):
  row_count=len(mat)
  col_count=len(mat[0])
  for i in range(1, row_count):
    for j in range(0, col_count):
      minPrev=sys.maxint
      for k in range(j-1, j+2):
        if k>=0 and mat[i-1, k]<minPrev:
          minPrev=mat[i-1, k]
      mat[i][j]=minPrev+mat[i][j]
  print mat
  return min(mat[row_count-1])

main()