class Solution(object):
    moves = "UD"
    def judgeCircle(self, moves):
        origin = [0,0]
        for i in range(len(moves)):
            if moves[i] == 'U':
                origin[0] += 1
            elif moves[i] == 'D':
                origin[0] -= 1
            elif moves[i] == 'R':
                origin[1] += 1
            elif moves[i] == 'L':
                origin[1] -= 1
        if origin[0] == 0 and origin[1] == 0:
            return True
        else:
            return False

            
