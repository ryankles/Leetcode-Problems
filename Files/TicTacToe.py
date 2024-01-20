class Solution(object):
    moves = [[2,2],[0,1],[2,1],[0,0],[0,2]]
    print(len(moves))
    def tictactoe(moves):
        if len(moves) == 9:
            return 'Draw'
        if len(moves) < 5:
            return 'Pending'
        elif len(moves) % 2 == 0:
            for i in range(len(moves)-1):
                value = moves[i+1][i]
                value2 = moves[i+1][i]
                if moves[i+1][i] == value:
                    return "B"
                elif moves[i+1][i+1] == value2:
                    return "B"
                
                else:
                    return 'Pending'
        else: 
            for i in range(len(moves)-3):
                value = moves[i][i]
                value2 = moves[i][i]
                if moves[i][i] == value:
                    return "A"
                elif moves[i][i+1] == value2:
                    return "A"
                else:
                    return 'Pending'
    print(tictactoe(moves))
