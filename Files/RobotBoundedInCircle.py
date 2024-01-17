class Solution(object):
    
    instructions = "LLGRL"
    
    def isRobotBounded(instructions):
        instructions += instructions + instructions + instructions
        print(instructions)
        plane = [0,0]
        print(plane)
        currDirection = 0
        north = 0
        west = 1
        south = 2
        east = 3
        for i in range(len(instructions)):
            if instructions[i] == 'L':
                if currDirection != 3:
                    currDirection += 1
                else:
                    currDirection -= currDirection
            elif instructions[i] == 'R':
                if currDirection != 3:
                    currDirection += 1
                else:
                    currDirection -= currDirection
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
        if plane == [0,0]:
            return True
        else: 
            return False
    print(isRobotBounded(instructions))

            
        
