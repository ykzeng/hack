"""
quick select top k
"""
def main():
  test=[8, 1, 14, 9, 15, 5, 4, 3, 7, 17, 11, 18, 2, 12, 16, 13, 6, 10]
  print test

  topk=select(test, 5)
  print topk

def select(arr, k):
  if k>len(arr):
    return arr;
  for i in range(0, k):
    maxVal=arr[i]
    maxIndex=i
    for j in range(i+1, len(arr)):
      if arr[j]>maxVal:
        maxVal=arr[j]
        maxIndex=j
    arr[maxIndex]=arr[i]
    arr[i]=maxVal
  return arr[0:k]

main()