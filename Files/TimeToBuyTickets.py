class solution:
    tickets = [84,49,5,24,70,77,87,8]
    k = 3
    def timeRequiredToBuy(tickets, k):
        time = 0
        for j in range(tickets[k]):
            for i in range(len(tickets)):
                if tickets[i] == 0:
                    continue
                else:
                    tickets[i] -= 1
                    if tickets[k] == 0:
                        break
                    time += 1
        return time

    print(timeRequiredToBuy(tickets, k))