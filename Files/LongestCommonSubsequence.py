class Solution:
    text1 = "abcde"
    text2 = "ace" 
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)
        count = 0
        if len1 <= len2:
            if text1 in text2:
                return len1
            else:
                for i in range(len1):
                    if text1[i] in text2:
                        text2.replace(text1[i], "")
                        count+=1
                return count    
        else:
            if text2 in text1:
                return len2
            else:
                for i in range(len2):
                    if text2[i] in text1:
                        text1.replace(text2[i], "")
                        count+=1
                return count    
    print(longestCommonSubsequence(text1, text2))