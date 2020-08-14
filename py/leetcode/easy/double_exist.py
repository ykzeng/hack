from typing import List

def checkIfExist(arr: List[int]) -> bool:
        d = {}
        for i in range(0, len(arr)):
            d[arr[i]] = i
        for i in range(0, len(arr)):
            n = arr[i]
            double = n*2
            if (double) in d and d[double] != i:
                return True
        return False
        # seen = set()
        # for i in arr:
        #   # if 2 * i in seen or i % 2 == 0 and i // 2 in seen:
        #     if 2 * i in seen or i / 2 in seen: # credit to @PeterBohai
        #         return True
        #     seen.add(i)
        # return False

print(checkIfExist(
[10,2,5,3]))
# [-2,0,10,-19,4,6,-8]