class Solution(object):
    s = "a"
    t = "aa"
    def findTheDifference(s, t):
        for i in range(len(t)):
            if t[i] not in s or t.count(t[i]) != s.count(t[i]):
                self = t[i]
                print(self)
                break
            
    findTheDifference(s, t)