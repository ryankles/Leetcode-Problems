class Solution(object):
    s = "anagram"
    t = "nagaram"
    self = False
    def isAnagram(self, s, t):
        if sorted(s) == sorted(t):
            self = True
        else:
            self = False
        
        print(self)
    isAnagram(self, s,t)