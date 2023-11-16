class Solution(object):
    nums = [0,1,0,3,12]
    def moveZeroes(nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        print(nums)
    moveZeroes(nums) 