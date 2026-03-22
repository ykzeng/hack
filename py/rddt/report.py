s="""a,b,c
b,d
d,e"""
from collections import defaultdict
reports={}
manages=defaultdict(list)
visited=set()
nodes=[]

# a->b, means a manages b
for line in s.split('\n'):
    arr=line.split(',')
    mgr=arr[0]
    nodes.extend(arr)
    for r in arr[1:]:
        reports[r]=mgr
    manages[mgr]+=arr[1:]
print(reports)
print(manages)

def dfs(n,depth=0):
    if n in visited:
        return
    visited.add(n)
    print('...'*depth+str(n))
    if n in manages:
        for rep in manages[n]:
            dfs(rep,depth+1)

# FIXME here we can use current index position
# of skip-boss to check how many '...' to be printed
def skip(cur,path=[]):
    # if cur=='e':
    #     print(path)
    # print(path)
    if len(path)>=2:
        tmp=path[-2:].copy()+[cur]
        tmp[1]+='[skip]'
        for i,n in enumerate(tmp):
            print('...'*i+str(n))
    if cur in manages:
        for rep in manages[cur]:
            skip(rep,path+[cur])

for n in nodes:
    if n not in reports:
        dfs(n)

for n in nodes:
    if n not in reports:
        # print(n)
        skip(n)