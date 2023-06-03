Block Maze Solver

Authors: Sean, Kyle, Tristan 

Description: This program is designed to solve rolling block maze puzzles using A* Search. 
The user has the option of using 2 different heuristics, manhattan and nt. The program takes
in a rolling block maze in the form of a .txt file where empty spaces are represented as '.', 
obstacles are represented by '*' and the starting and goal blocks are represented by 'S' and 'G' repectively.

To run the program, 
    "python3 blockmaze.py ~pathwayToMazeFile~ heuristic(manhattan/nt)"
     
     Ex. To run maze2.txt with a manhattan distance heuristic, 
         python3 blockmaze.py examples/maze2.txt manhattan

         To run maze2.txt with a trivial heuristic, 
         python3 blockmaze.py examples/maze2.txt nt
