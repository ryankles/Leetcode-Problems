class Solution(object):
    arr = [3,5,1]   
    def canMakeArithmeticProgression(arr):
        arr.sort
        
        temp = arr[0] - arr[1]
        for i in range(len(arr)-1):
            if arr[i] - arr[i+1] == temp:
                continue
            else:
                return False

    canMakeArithmeticProgression(arr)