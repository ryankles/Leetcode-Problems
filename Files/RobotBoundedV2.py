class Solution(object):
    
    instructions = "GGLLGG"
    
    def isRobotBounded(instructions):
        plane = [0,0]
        currDirection = 1
        
        north = 1
        west = 2
        south = 3
        east = 4
        
        for i in range(len(instructions)):
            if instructions[i] == 'L':
                if currDirection != 4:
                    currDirection -= 1
                else:
                    currDirection = 0
            elif instructions[i] == 'R':
                if currDirection != 4:
                    currDirection += 1
                else:
                    currDirection = 0
            elif instructions[i] == 'G':
                if currDirection == north:
                    plane[1]+=1
                    print(plane)
                if currDirection == east:
                    plane[0]+=1
                    print(plane)
                if currDirection == south:
                    plane[1]-=1
                    print(plane)
                if currDirection == west:
                    plane[0]-=1
                    print(plane)
        return(plane)
    print(isRobotBounded(instructions))
