class Solution(object):
    haystack = "leetcode"
    needle = "leeto"
    def strStr(haystack, needle):
        tempVal = 0
        self = 0
        if needle in haystack:
            while tempVal < len(haystack):
                self = haystack.find(needle, tempVal, len(haystack))
                tempVal += len(needle) + 1
                if self == -1:
                    return
                print(self)
        else:
            self = -1
        print(self)
    strStr(haystack, needle)
            