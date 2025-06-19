# Problem: Sudoku

## Description
The generator takes in 1 argument from the user, the number of cells to remove (`n`). The generator uses a 
[Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search) algorithm to generate random sudoku boards,
then removes the appropraite number of cells.

The user should note that removing too many cells may result in more than one solution to the board. We view this as
a strength to the solver, being able to find many different solutions, should they exist.
