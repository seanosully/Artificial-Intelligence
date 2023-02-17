# Sean, Kyle, Tristan
# Prof. Fitzsimmons
# Artificial Intelligence
# Project 1 
# 
# Description: 
# Program finds the optimal path in a rolling block maze given a specific heuristic. 
# The program can be run with "python3 blockmaze.py examples/maze_.txt heuristicType(manhattan/nt)
# 
from inspect import currentframe
from re import I
import sys
import heapq

class Node: # Define our node class
    def __init__(self, parent= None, position= None, standing = None):
        
        self.standing = standing # standing state
        self.parent = parent     # store parent node
        self.position = position # position of the node in tuple coordinates ((x1,y1),(x2,y2))
        self.h = 0 # estimated cost to goal from n
        self.g = 0 # cost so far to reach n
        self.f = 0 # estimated total cost of path through n to goal

    def __eq__(self, other):
        return self.position == other.position 
    #overload functions
    def __lt__(self, other):
        return self.f < other.f
# Read maze file and store the different aspects of it:
# Start Node, Goal Node, All of the Obstacles, etc. 
def read_file(filename): 
    print("reading " + filename)

    x = 0
    y = 0
    obstacles = []

    maze = open(filename)

    mazeArray = []
    numRows = 0 
    for row in maze:
        for char in row:

            if char == 'S':
                startPosition = ((x,y),(x,y)) # store in tuple

            if char == 'G':
                goalPosition = ((x,y),(x,y))  # store in tuple

            if char == '*':
                obstacles.append((x,y))       # obstacle not in tuple because it is only one square

            x = x+1
        x = 0
        y = y+1

        row = row.rstrip('\n')
        mazeArray.append(row) 
        print (row)
        numRows += 1
    return mazeArray, startPosition, goalPosition, obstacles, numRows # return values to A_STAR

# Function that dictates the next moves given the block's current position. 
def Actions(node, maze, obstacles, rows):
    actions= []
    if node.standing is True: # if the block is standing, do these certain moves. 
        moves= [(((node.position[0][0]+ 1),(node.position[0][1]+ 0)), ((node.position[1][0]+ 2),(node.position[0][1]+0))), 
                (((node.position[0][0] + 0),(node.position[0][1]+ 1)), ((node.position[1][0] + 0),(node.position[1][1]+2))), 
                (((node.position[0][0]- 1),(node.position[0][1]+ 0)), ((node.position[1][0]- 2),(node.position[0][1]+0))), 
                (((node.position[0][0] + 0),(node.position[0][1]- 1)), ((node.position[1][0] + 0),(node.position[1][1]-2)))]
        #print("This is moves", moves)
        for currentMove in moves:
            currentMoveIsObs = False 
            #check if out of bounds or if on obstacle
            if (currentMove[0][0] < 0 or currentMove[1][0] < 0) or (currentMove[0][0] > len(maze)-1 or currentMove[1][0] > len(maze)-1):
                continue
            if (currentMove[0][1] < 0 or currentMove[1][1] < 0) or (currentMove[0][1] > rows-1 or currentMove[1][1] > rows-1):
                continue 
            for obs in obstacles: #check if the move is on an obstacle
                if currentMove[0] == obs or currentMove[1] == obs:
                    currentMoveIsObs = True # if currNode is obstacle then set flag to true to tell program to break out of loop
                    break
            if currentMoveIsObs is True: 
                continue

            nextMove= Node(node, currentMove, False)
            actions.append(nextMove)
    else: #laying down horizontally
        if node.position[0][1]== node.position[1][1]:    
            if node.position[0][0] < node.position[1][0]: 
                moves= [(((node.position[0][0]+ 2),(node.position[0][1]+ 0)), ((node.position[1][0]+ 1),(node.position[1][1]+ 0))), #move right to stand
                        (((node.position[0][0]- 1),(node.position[0][1]+ 0)), ((node.position[1][0]- 2),(node.position[1][1]+ 0))), #move left to stand
                        (((node.position[0][0]+ 0),(node.position[0][1]+ 1)), ((node.position[1][0]+ 0),(node.position[1][1]+ 1))), #roll down
                        (((node.position[0][0]+ 0),(node.position[0][1]- 1)), ((node.position[1][0]+ 0),(node.position[1][1]- 1)))] #roll up
            else: 
                moves= [(((node.position[0][0]+ 1),(node.position[0][1]+ 0)), ((node.position[1][0]+ 2),(node.position[1][1]+ 0))), #move right to stand
                        (((node.position[0][0]- 2),(node.position[0][1]+ 0)), ((node.position[1][0]- 1),(node.position[1][1]+ 0))), #move left to stand
                        (((node.position[0][0]+ 0),(node.position[0][1]+ 1)), ((node.position[1][0]+ 0),(node.position[1][1]+ 1))), #roll down
                        (((node.position[0][0]+ 0),(node.position[0][1]- 1)), ((node.position[1][0]+ 0),(node.position[1][1]- 1)))] #roll up 
        else: # laying down vertically
            if node.position[0][1] < node.position[1][1]: 
                moves= [(((node.position[0][0]+ 0),(node.position[0][1]+ 2)), ((node.position[1][0]+ 0),(node.position[1][1]+ 1))), #move up to stand
                        (((node.position[0][0]+0),(node.position[0][1]-1)), ((node.position[1][0]+0),(node.position[1][1]-2))),  # move down to stand
                        (((node.position[0][0]- 1),(node.position[0][1]+ 0)), ((node.position[1][0]- 1),(node.position[1][1]+ 0))), # roll left
                        (((node.position[0][0]+ 1),(node.position[0][1]+0)), ((node.position[1][0]+1),(node.position[1][1]+0)))] # roll right
            else: 
                moves= [(((node.position[0][0]+ 0),(node.position[0][1]+ 1)), ((node.position[1][0]+ 0),(node.position[1][1]+ 2))), #move up to stand
                        (((node.position[0][0]+0),(node.position[0][1]-2)), ((node.position[1][0]+0),(node.position[1][1]-1))),     # move down to stand
                        (((node.position[0][0]- 1),(node.position[0][1]+ 0)), ((node.position[1][0]- 1),(node.position[1][1]+ 0))), # roll left 
                        (((node.position[0][0]+ 1),(node.position[0][1]+0)), ((node.position[1][0]+1),(node.position[1][1]+0)))]    # roll right
        for currentMove in moves:
            currentMoveIsObs = False 
            #check if out of bounds or if on obstacle
            if (currentMove[0][0] < 0 or currentMove[1][0] < 0) or (currentMove[0][0] > len(maze)-1 or currentMove[1][0] > len(maze)-1):
                continue
            if (currentMove[0][1] < 0 or currentMove[1][1] < 0) or (currentMove[0][1] > rows-1 or currentMove[1][1] > rows-1):
                #print("Going in here")
                continue
            
            for obs in obstacles: #check if the move is on an obstacle
                if currentMove[0] == obs or currentMove[1] == obs:
                    currentMoveIsObs = True
                    break

            if currentMoveIsObs is True: # if the current move is on an obstacle, move to the next possible move. 
                continue
            
            if currentMove[0][0]== currentMove[1][0] and currentMove[0][1]!= currentMove[1][1]: # seeing if the next move will be set to standing
                nextMove= Node(node, currentMove, False)
                actions.append(nextMove)
            if currentMove[0][0]!= currentMove[1][0] and currentMove[0][1]== currentMove[1][1]: # seeing if the next move will be set to standing
                nextMove= Node(node, currentMove, False)
                actions.append(nextMove)
            if currentMove[0][0]== currentMove[1][0] and currentMove[0][1]== currentMove[1][1]: # seeing if the next move will be set to standing
                nextMove= Node(node, currentMove, True)
                actions.append(nextMove)    
    
    return actions # Returns list of nodes as actions

# Function to calculate heuristic values based on user arguments
def heuristicChoice(current, goal):
    if heur == "manhattan": # if manhattan distance 
        if current.standing is True: 
            heuristic = ((abs(current.position[0][0]-goal.position[0][0]))    # if its standing we only need to look at one node, thus we calc the dist 
                    +(abs(current.position[0][1]-goal.position[0][1])))*(2/3) # b/w the x and y of the current and goal nodes 
        else: 
            heuristic = max(((abs(current.position[0][0]-goal.position[0][0])    # else if it is lying, we look at the distance that is further away
                        +abs(current.position[0][1]-goal.position[1][1]))*(2/3)), 
                        ((abs(current.position[1][0]-goal.position[0][0])
                        +abs(current.position[1][1]-goal.position[1][1]))*(2/3)))
        return heuristic
    elif heur == "nt":  # if trivial heursitic, then do this
        if current.standing:
            return 0
        else:
            return 1 

# astar function that takes StartNode, GoalNode, MazeNode, ObstaclesNode, Amount of Nodes
def A_STAR(startingPosition, goalPosition, maze, obstacles, rows): 
    frontier = []
    explored= [] # if we revisit same exact state we've made a mistake, fine if we are on same tile as before, must be in different orientation though
    nodesGenerated= 0 # 
    path = []
    start= Node(None, startingPosition, True) # store startnode position into new node
    goal= Node(None, goalPosition, True)      # store goalnode position into new node
    start.g= 0                                # store g 
    start.h = int(heuristicChoice(start, goal)) # store heuristic value
    start.f= start.g + start.h                # store f value in start
    goal.h= 0
    goal.g= 0
    goal.f= 0
    
    if start.position == goal.position: #if start poistion and goal position are the same return
        return start
    
    frontier.append(start) #append starting node to frontier

    while frontier: # only run loop if the frontier is not empty  
        heapq.heapify(frontier)              # heapify frontier
        currentNode= heapq.heappop(frontier) # pop off the frontier and store it 
        explored.append(currentNode)         # append to explored set
        nodesGenerated = nodesGenerated + 1  # track of the number of nodes generating

        if (currentNode.position == goal.position):  # reached goal state condition
            print("Nice job! Goal Reached")
            while currentNode is not None:           # go up the "tree" of parents to get path
                path.append(currentNode.position)
                currentNode = currentNode.parent 
            path.reverse() # reverse the path to make it readable
            print("Moves in path: " + str(len(path) - 1))
            print("Number of nodes: " + str(nodesGenerated))
            print("Number of explored nodes: " + str(len(explored)))
            return path # return path to be printed

        actions= Actions(currentNode, maze, obstacles, rows) # get possible moves from the current node
        for posMove in (actions):                                              # go through the possible moves and find the children of each node 
            child = Node(posMove.parent, posMove.position, posMove.standing)   # to find an optimal or any path
            child.h = int(heuristicChoice(child, goal))
            child.g = currentNode.g+1
            child.f = child.g + child.h # update the heuristics
            
            if (child not in frontier) and (child not in explored): # make sure children are not in frontier nor explored
                heapq.heappush(frontier,child)                      # push child to frontier
                nodesGenerated = nodesGenerated+1                   # keep track of the nodes generated
            elif child in frontier:                                 # if the child is in the frontier, then we wanna
                temp = frontier.pop()                               # compare the child's f value with the temp's f value 
                if(child.f < temp.f):
                    heapq.heapify(frontier)                         # if the child's f value is less than the temp's f value, then heapify the frontier
                    heapq.heappush(frontier,child)
                else:
                    frontier.append(temp)                           # otherwise the temp is less than child, so append that to frontier to be explored
    return None

# Main Function that calls our functions
def main():  
    if len(sys.argv) != 3: # make sure user inputs correct amount of arguments, otherwise exit
        print("Usage: python3 blockmaze.py mazeFile heuristicType")
        sys.exit(1)
    else:
        dictionaryFile = sys.argv[1]   
        global heur # to be used in the HeuristicChoice function we created
        heur = sys.argv[2]
        if heur != "manhattan" and heur != "nt": #make sure the user inputted a correct heurisitic
            print(heur) 
            print("Heurisitc is either 'manhattan' or 'nt'")
            sys.exit(1)
        maze, start, goal, obstacles, rows = read_file(dictionaryFile) #store variables to be read into A_Star
        path_to_goal= A_STAR(start, goal, maze,obstacles, rows)
    print()                         # Print statements to show the results of our program 
    print("Starting coordinates")   # Gives us a stats regarding the path, start, end, and the obstacles.
    print(start)
    print("Goal coordinates")
    print(goal)
    print("Obstacles")
    print(obstacles)
    print("This is the path to goal:")
    print(path_to_goal)
       

if __name__ == "__main__":
    main()