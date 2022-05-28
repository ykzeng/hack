def nextPermutation(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = -1
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            left = i
    if left == -1:
        nums.reverse()
    maxv, maxi = -float("inf"), len(nums)
    for i in range(len(nums) - 1, left, -1):
        if nums[i] > nums[left] and nums[i] > maxv:
            maxv, maxi = nums[i], i
    nums[left], nums[maxi] = nums[maxi], nums[left]
    # return nums[: left + 1] + nums[left + 1 :][::-1]


print(nextPermutation([3, 2, 1]))
