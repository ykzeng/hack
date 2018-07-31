def main():
  test=[8, 1, 14, 9, 15, 5, 4, 3, 7, 17, 11, 18, 2, 12, 16, 13, 6, 10]
  print test

  sorted_arr=qsort(test, 0, len(test))
  print sorted_arr

def qsort(arr, lo, hi):
  if lo < hi:
    pivot=partition(lo, hi, arr)
    qsort(arr[lo:pivot], lo, pivot)
    qsort(arr[pivot:hi], pivot, hi)

def partition(lo, hi, arr):
  pVal=arr[hi]
  i=lo-1
  for j in range(lo, hi):
    if arr[j]<pVal:
      i+=1
      swap(arr, i, j)
  swap(arr, i+1, hi)
  return (i+1)
  
def swap(arr, i, j):
  tmp=arr[i]
  arr[i]=arr[j]
  arr[j]=tmp

main()