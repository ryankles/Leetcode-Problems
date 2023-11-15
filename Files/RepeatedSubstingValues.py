class Solution(object):
    s = 'a'
    self = True
    def repeatedSubstringPattern(self, s):
        newString = s[1:len(s)] + s[0]
        if len(s) == 1:
            self = True
        else:
            for i in range(len(s)-1):
                if newString != s:
                    newString += newString[0]
                    newString = newString[1:len(newString)]
                    self = False
                else:       
                    self = True
        print(self)
                
            

    repeatedSubstringPattern(self, s)