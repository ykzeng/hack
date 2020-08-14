# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
# Example 1:
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
# Input: [[7,10],[2,4]]
# Output: 1

def meeting_room(slots):
    slots = sorted(slots)
    for i in range(0, len(slots)-1):
        n = i + 1
        m1 = slots[i]
        m2 = slots[n]
        if m2[0] < m1[1]:
            return False
    return True


samples = [[[0, 30], [5, 10], [15, 20]], [[7, 10], [2, 4]]]
for s in samples:
    print("test case: "+str(s))
    print("has meeting room: "+str(meeting_room(s)))
