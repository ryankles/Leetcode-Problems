class Solution(object):
    arr = [3,5,1]   
    def canMakeArithmeticProgression(self, arr):
        newArr = arr.sort()
        def runAgain(self, temp):
            for i in range(len(temp)-2):
                if temp[i] - temp[i+1] != temp[i+1] - temp[i+2]:
                    self = False
                else:
                    self = True
        if runAgain(arr) == True:
            return self
        elif runAgain(arr) == False:
            arr.sort()
            runAgain(arr)
        



    canMakeArithmeticProgression(arr)