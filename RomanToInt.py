class Solution(object):
    s = ("MCMXCIV")
    def romanToInt(s):
        numeralDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        finalVal = 0
        for i in range(len(s)-1):
            if s[i] in numeralDict:
                if numeralDict[s[i]] < numeralDict[s[i+1]]:
                        finalVal = finalVal + (numeralDict[s[i+1]] - numeralDict[s[i]])
                        print(f"If value: {numeralDict[s[i]]} \nPrintval: {finalVal}")
                        print(i)
                        break
                else:
                    finalVal = finalVal + numeralDict[s[i]]
                    print(f"Else value: {numeralDict[s[i]]} \nPrintval: {finalVal}")
                    print(i)


        #finalVal = finalVal + numeralDict[s[i]]
        print(finalVal)
    romanToInt(s)