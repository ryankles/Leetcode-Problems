class Solution(object):
    def twoSum(self, nums, target):
        newVal = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    newVal.append(i)
                    newVal.append(j)
                    return newVal