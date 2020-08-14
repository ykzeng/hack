# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.
# Example 1:
# Input: [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
# Input: [[7,10],[2,4]]
# Output: true
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

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
