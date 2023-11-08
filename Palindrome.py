class Solution(object):
    x = 121
    def isPalindrome(x):
        x = str(x)
        n = x[::-1]
        if n == x:
            print('True')
        else:
            print('False')
    
        
        
        
        
        # for i in range(len(x)-1):
        #     if x[i] == x[len(x)-1-i] and i != len(x)    -i:
        #         print(f"well {x[i]} {x[len(x)-1-i]}")
        #     else:
        #         print(f"wrong {x[i]} {x[len(x)-1-i]}")
        #         break
        #     ++i
    isPalindrome(x)