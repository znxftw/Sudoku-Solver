# Sudoku-Solver

A program to solve Sudoku puzzles without brute force. Uses boolean multidimensional lists.

Note : When giving input for x,y , note that origin is (0,0) and not (1,1) as traditionally referred to by Sudoku solvers.
Method of approach :
- boolean list stores 'True' for possibility of a value existing at a given space.

  - Populate boolean list with initial known values
  - Eliminate row,column,box possibilities of current grid
  - Update grid with certain values
  - If no elimination possible, assume a value at a grid and reattempt solving
 
I've tested out the program on multiple easy/medium/hard puzzles and they all worked out. Kindly let me know if it doesn't on a certain one.
