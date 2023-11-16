class Solution(object):
    nums = [-1,-2,-3,-4,3,2,1]   
    def signFunc(x):
        if x > 0:
            x = 1
        elif x < 0:
            x = -1
        else:
            x = 0
    def arraySign(nums):
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
        signFunc(product)
    
    print(arraySign(nums))
    
    
            