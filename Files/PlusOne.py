class Solution(object):
    digits = [9,9,9]
    def plusOne(digits):
        dictionary = ['0','1','2','3','4','5','6','7','8','9']
        newVal = ""
        for i in range(len(digits)):
            newVal += dictionary[digits[i]]
            print(type(newVal))
        newVal = int(newVal)
        print(type(newVal))
        newVal += 1
        newVal = str(newVal)
        print(type(newVal))
        print(len(newVal))
        print(newVal)
        digits = []
        for i in range(len(newVal)):
            digits.append(newVal[i])
            
        print(digits)

    plusOne(digits)