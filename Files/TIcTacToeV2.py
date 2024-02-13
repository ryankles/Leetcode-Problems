class Solution(object):
    moves = [[1,0],[2,2],[2,0],[0,1],[1,1]]
    print(len(moves))
    new = 'A'
    def tictactoe(moves):
        if len(moves) == 9:
            return 'Draw'
        elif len(moves) < 5:
            return 'Pending'
        print(moves)
        lip = 0
        if len(moves) % 2 != 0:
            lip = 5
            new = 'B'
            print(moves)
        temp = int(len(moves) / 2)
        for lip in range(temp):
            moves.pop(lip-1)
            lip += 2
        
            
        return moves
        # if moves[0][len(moves)] == 
    print(tictactoe(moves))