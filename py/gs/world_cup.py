"""
OA
given the predicted goals of each team in a group
calc the possibility of randomly wactched the match with highest goals among all
"""
def main():
  team_goals=[2, 4, 1, 3, 7, 7, 5]
  print probability(team_goals)

def probability(team_goals):
  team_count=len(team_goals)
  tot_match=permuation(team_count, 2)
  print "total match permutations: "+str(tot_match)
  #sorted_tgoals=qsort(team_count, 0, len(team_goals))
  topk_goals, topk_counts=getklarge(team_goals, 2)
  print "top k avg goal count among teams in this group: "+str(topk_goals)
  print "how many teams get the top k goals: "+str(topk_counts)
  if topk_counts[0]==1:
    return (float(topk_counts[1])/tot_match)
  elif topk_counts[0]>1:
    return (float(permuation(topk_counts[0], 2))/tot_match)
  else:
    return None
  
def permuation(tot, select):
  return factorial(tot)/(factorial(tot-select)*factorial(select))

def getklarge(arr, k):
  count_lst=[]
  if k>len(arr):
    return arr;
  for i in range(0, k):
    maxVal=arr[i]
    maxIndex=i
    count=1
    for j in range(i+1, len(arr)):
      if arr[j]>maxVal:
        maxVal=arr[j]
        maxIndex=j
        count=1
      elif arr[j]==maxVal:
        count+=1
    count_lst.append(count)
    arr[maxIndex]=arr[i]
    arr[i]=maxVal
  return arr[0:k], count_lst

def qsort(arr, lo, hi):
  if lo < hi:
    pivot=partition(arr, lo, hi)
    qsort(arr, lo, pivot-1)
    qsort(arr, pivot+1, hi)
  return arr

def partition(arr, lo, hi):
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

def factorial(n):
  fac=1
  for i in range(1, n+1):
    fac=fac*i
  return fac

main()