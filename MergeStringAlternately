class Solution(object):
    word1 = "abcde"
    word2 = "xyz"
    def mergeAlternately(word1, word2):
        newWord = ""
        length = int()
        if len(word1) <= len(word2):
            length = len(word1)
            reality = True
        else: 
            length = len(word2)
            reality = False
        for i in range(length):
            newWord = newWord + word1.join(word1[i])
            newWord = newWord + word2.join(word2[i])
        if reality is True:
            for j in range(len(word2) - length):
                newWord = newWord + word2[j+length]
        if reality is False:
            for j in range(len(word1) - length):
                newWord = newWord + word1[j+length]
        print(f"\"{newWord}\"")
    mergeAlternately(word1, word2)
        