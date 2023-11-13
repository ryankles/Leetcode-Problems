class Solution(object):
    haystack = "sadbutsad"
    needle = "sad"
    location = ""
    def strStr(haystack, needle):
        tempVal = 0
        if needle in haystack:
            for i in range(len(haystack)):
                location = haystack.index(needle, tempVal, len(haystack))
                print(location)

    strStr(haystack, needle)
            