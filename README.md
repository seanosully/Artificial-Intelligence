Project \#1 Rolling Block Mazes
-------------------------------

# Introduction

In this project you will work in groups three to write a Python program to solve rolling block mazes
using A\* search.
In a rolling block maze ([http://www.logicmazes.com/rb/column.html][maze]), you are presented with a grid with obstacles, a starting location, and an ending location.
The object of the maze is to roll a 2x1x1 block (two spaces long and one space wide) through the
maze from the starting location with the block in an upright orientation (i.e., occupying one space) to the ending location with the block in an upright orientation, while avoiding obstacles.

[maze]:http://www.logicmazes.com/rb/column.html

Your program should read in a maze from a textfile given as a command-line argument and perform A\*
search. You must implement at least two admissible heuristics (at least one of these must be nontrivial).
Your search function must take an initial state, a goal state, and a description of the problem as input and
return the path of states found from the initial state to the goal state. Note that if
no solution exists, this path should be empty.
Along with the path, your search function must return the number of nodes generated (i.e., added to the frontier)
and the number of nodes visited during the search. Using this search function, given a maze and a choice of heuristic, your
program should print out the following.
* The path of states form the initial state to the goal state, or that none exists.
* The length of this path.
* The number of nodes generated during the search.
* The number of nodes visited during the search.

Five mazes have been included below (and textfiles for each are included in the starter code on github).
In each maze, "`S`" represents the start location, "`G`" represents the goal location, "`.`" represents an empty space,
and "`*`" represents an obstacle.

**Maze 1**
```
S......
.......
...*...
....*..
.....*.
..*....
......G
```

**Maze 2** [Source][maze2]
```
.....
S*...
.....
..*..
..G..
```

**Maze 3**
```
......*..
.......G.
....*..*.
....*....
...*.....
.........
...S.....
.........
```

**Maze 4**
```
....*..
S.*.G..
..*....
...*...
*......
.......
.......
```

**Maze 5** [Source][maze5]
```
.....*..
.**.....
.....*..
.GS*....
*..*...*
*.*..*..
....*...
........
```

[maze2]: http://www.puzzlebeast.com/rollingblock/
[maze5]: http://www.logicmazes.com/rb/blockmz.html

## Writeup

Along with submitting your code, your group must also submit a 2--3 page writeup that contains the following:
  * A description of the search problem. Make sure to include the initial state, goal test, actions, and path
  cost in your description.
  * Formal definitions for each of your heuristics, what they are attempting to measure,
  and why they are admissible.
  * For each of the mazes included above, list in a table the results of running your program, i.e., the number
  of nodes generated and the number of nodes visited, for each of your heuristics.
  * A discussion of your results, including how your heuristics compared to one another, your thoughts
  on why each heuristic may have helped to guide the search more on one puzzle than another,
  and if this was consistent with what you expected.

## Checkpoint

As a project checkpoint, you must schedule a time for your group to meet with me to discuss your
initial implementation and your plans for the project by Friday, September 16. Note that you should
have at least the initial parts of your project implemented by this meeting (e.g., reading in the
mazes, node representation, etc) and should be prepared to discuss your plans for finishing the
project. Failure to schedule and attend this meeting will result in a penalty on your project
grade.

## Submission

Make sure to commit to your team's github repository as you make changes to your project. The project is due Friday, September 23 at 9:00 PM. A complete
submission consists of the following files.
  * Your writeup as a single PDF file, which must be named `project1.pdf`.
  * Your source code as `blockmaze.py`.
  * A short textfile that describes how to run your program as `readme.txt`.
  * Your discussion log as `discussion.txt`.

When you are ready to submit your assignment, create a "Release" on github. This will tag the commit
and make a downloadable archive of the state of the files. I will grade the most-recent release created
within the deadline (or late deadline when submitting late). Note that if you are using github throughout your
development process, you should only need to create your release once for the deadline, since your incremental
progress will be saved in the commit history.

## Grading
  * Correctness (A\* implementation, heuristics, correctness of search): 50 points.
  * Code clarity/efficiency: 15 points.
  * Writeup: 35 points.

Programming Style: You will be graded
not only on whether your program works correctly, but also on
programming style, such as the use of informative names, good
comments, easily readable formatting, and a good balance between
compactness and clarity (e.g., do not define lots of unnecessary
variables). Create appropriate
functions for tasks that can be encapsulated.
