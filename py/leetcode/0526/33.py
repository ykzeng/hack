class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)
        while lo<hi:
            mid=lo+(hi-lo)//2
            if((target<nums[0]) == (nums[mid]<nums[0])):
                cur=nums[mid]
            elif target<nums[0]:
                cur=-sys.maxsize
            else:
                cur=sys.maxsize
            if cur==target:
                return mid
            elif cur<target:
                lo=mid+1
            else:
                hi=mid
        return -1