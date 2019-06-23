grades=[["A", "87"], ["B", "60"], ["C","22"],["C","100"]]

def findHighAvg(arr):
    summary = {}
    for g in arr:
        k = g[0]
        v = int(g[1])
        if k in summary:
            vs = summary.get(k)
            vs.append(v)
        else:
            vs = [v]
            summary[k]=vs
    v_max = 0
    p = ''
    for k in summary.keys():
        vs = summary.get(k)
        v_avg = sum(vs) / len(vs)
        if v_avg > v_max:
            v_max = v_avg
            p = k
        summary[k] = v_avg
    print(summary)
    return p, v_max
    
print(findHighAvg(grades))