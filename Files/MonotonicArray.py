class Solution(object):
    nums = [2,3,4,1]
    def isMonotonic(nums):
        new = sorted(nums)
        print(new)
        new2 = new[::-1]
        if nums != new or nums != new2:
            print("false")
            break
        print("true")        
    isMonotonic(nums)