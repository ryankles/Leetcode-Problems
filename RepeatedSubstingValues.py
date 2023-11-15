class Solution(object):
    s = 'abab'
    def repeatedSubstringPattern(s):
        newString = s[1:len(s)] + s[0]
        print(newString)
        for i in range(len(s)):
            print(newString)
            if newString == s:
                print('true')
                return True
            else: 
                
                newString += newString[0]
                newString = newString[1:len(newString)]
                print(newString)
                print('false')
                return False
            

    repeatedSubstringPattern(s)