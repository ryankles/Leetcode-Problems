class Solution(object):
    operations = ["5","2","C","D","+"]
    def calPoints(self, operations):
        list = []
        tempNum = 0
        for i in range(len(operations)):
            if operations[i].isdigit() or operations[i].startswith('-'):
                tempNum = int(operations[i])
                list.append(tempNum)
            elif operations[i].isalpha():
                if operations[i] == 'D':
                    list.append((list[len(list)-1]) * 2)
                else:
                    list.pop(len(list)-1)
            else:
                list.append((list[len(list)-1]) + (list[len(list)-2]) )
        return sum(list)

    calPoints(operations)
                
            
                