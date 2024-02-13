class Solution:
    temperatures = [73,74,75,71,69,72,76,73]
    def dailyTemperatures(temperatures):
        answer = []
        for i in range(len(temperatures)):
            for j in range(len(temperatures)-i):
                if temperatures[i] < temperatures[j+i]:
                    answer.append(j)
                    break
                elif j+i == len(temperatures)-1:
                    answer.append(0)
                    
        return answer
    print(dailyTemperatures(temperatures))
