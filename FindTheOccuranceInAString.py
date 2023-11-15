class Solution(object):
    haystack = "leetcode"
    needle = "leeto"
    def strStr(haystack, needle):
        if needle in haystack:
            self = haystack.find(needle, 0, len(haystack))
        else:
            self = -1
        return self
    strStr(haystack, needle)
            