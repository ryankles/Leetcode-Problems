class Solution:
    words = ["abc","car","ada","racecar","cool"]
    def firstPalindrome(words):
        for i in range(len(words)):
            newWord = words[i][::-1]
            if newWord == words[i]:
                return words[i]
                break
            newWord = ''
        return ""
                

    print(firstPalindrome(words))