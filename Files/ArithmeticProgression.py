class Solution(object):
    arr = [3,5,1]   
    def canMakeArithmeticProgression(arr):
        arr.sort
        newArray =  arr[::-1]
        print(arr)
        print(newArray)
        isAri(arr)
        def isAri(newString):
            temp = newString[0] - newString[1]
            for i in range(newString):
                if newString[i+2] - newString[i+3] == temp:
                    print("true")
                else:
                    print("false")
                    break

                
        



    canMakeArithmeticProgression(arr)