class Solution(object):
    s = ("MCMXCIVM")
    def romanToInt(s):
        numeralDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        finalVal = 0
        for i in range(len(s)):
            if s[i] in numeralDict:
                if s[i] == "I" or "X" or "C" and len(s) != i:
                        ++i
                        finalVal = finalVal + (numeralDict[s[i+1]] - numeralDict[s[i]])
                else:
                    finalVal = finalVal + numeralDict[s[i]]
            ++i
        print(finalVal)
    romanToInt(s)