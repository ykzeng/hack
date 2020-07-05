vec1 = [1,2,3,4,5]

height = [0,1,0,2,1,0,1,3,2,1,2,1]
h2 = [2,0,2]
def threeSum(nums):
    nums.sort()
    res = []
    for i in range(0, len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        l = i + 1
        r = len(nums) - 1
        while l < r:
            tmpSum = nums[l] + nums[r] + nums[i]
            if tmpSum > 0:
                r -= 1
            elif tmpSum < 0:
                l += 1
            else:
                res.append([nums[l], nums[r], nums[i]])
                while l < r and nums[l+1] == nums[l]:
                    l += 1
                while l < r and nums[r-1] == nums[r]:
                    r -= 1
                l += 1
                r -= 1
    return res
# print(trap(height))
# print(trap(h2))

print(threeSum([-1, 0, 1, 2, -1, -4]))