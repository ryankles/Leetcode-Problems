class Solution(object):
    nums = [-1,-2,-3,-4,3,2,1]   
    def arraySign(nums):
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
        if product > 0:
            product = 1
        elif product < 0:
            product = -1
        else:
            product = 0
        return(product)
    print(arraySign(nums))
    
    
            