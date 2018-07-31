"""
OA
a company donates money to three charities A, B, C
rule of donation: 
1. donate to the one who get least from the company in total
2. if all get equal share in the past, donate based on alphabetic order A->B->C
"""

def main():
    mon_profits = [25, 8, 2, 35, 15, 120, 55, 42]
    sequence = donate(mon_profits)
    print sequence


def donate(profits):
    comp_map = {0: "A", 1: "B", 2: "C"}
    sum_donations = [0, 0, 0]
    sequence = []
    for p in profits:
        leastCompIndex, leastAmount = findMin(sum_donations)
        sum_donations[leastCompIndex] += p
        sequence.append(comp_map[leastCompIndex])
    return sequence


def findMin(arr):
    if len(arr) == 0:
        return None
    minVal = arr[0]
    minIndex = 0
    for i in range(0, len(arr)):
        if minVal > arr[i]:
            minVal = arr[i]
            minIndex = i
    return minIndex, minVal

main()