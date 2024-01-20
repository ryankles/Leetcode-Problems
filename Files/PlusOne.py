class Solution(object):
    digits = [9,9,9]
    def plusOne(self, digits):
        dictionary = ['0','1','2','3','4','5','6','7','8','9']
        newVal = ""
        for i in range(len(digits)):
            newVal += dictionary[digits[i]]
        newVal = int(newVal)
        newVal += 1
        newVal = str(newVal)
        digits = []
        for i in range(len(newVal)):
            digits.append(newVal[i])
    plusOne(digits)