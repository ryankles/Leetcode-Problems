class Solution(object):
    operations = ["5","2","C","D","+"]
    def calPoints(operations):
        list = []
        tempNum = 0
        for i in range(len(operations)):
            if operations[i].isdigit() == True:
                tempNum = int(operations[i])
                list.append(tempNum)
                print(list)
            elif operations[i].isalpha() == True:
                if operations[i] == 'D':
                    list.append((list[len(list)-1]) * 2)
                    print(list)
                else:
                    list.pop(i-1)
                    print(list)
            else:
                list.append((list[len(list)-1]) + (list[len(list)-2]) )
                print(list)
        sum(list)
        print(sum(list))
        return list
            

    calPoints(operations)
                
            
                