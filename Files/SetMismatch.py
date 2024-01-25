class Solution(object):
    nums = [1,5,3,2,2,7,6,4,8,9]
    def findErrorNums(nums):
        new = [0,0]
        temp = 1
        newTemp = 1
        nums.sort()
        print(nums)
        for i in range(len(nums)): 
            if nums.count(temp) == 2:
                new[0] += nums[i]
                nums.pop(i)
                for j in range(len(nums)):
                    if nums[j] != newTemp:
                        new[1] = newTemp
                        break
                    newTemp+=1
                new[1] = newTemp
                break
            temp+=1
            
        return new


    print(findErrorNums(nums))
            
            