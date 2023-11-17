class Solution(object):
    nums = [3,5,2,3]
    def minPairSum(nums):
        nums.sort()
        max = len(nums) - 1
        temp = 0
        for i in range(len(nums)):
            if temp < nums[i] + nums[max]:
                temp = nums[i] + nums[max]
            max += 1
        return temp
            
    minPairSum(nums)