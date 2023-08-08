%*
 * File: sudoku.lp
 * Author: Joshua T. Guerin
 *
 * Description: Implementation of the sudoku puzzle problem.
 * Use: clingo sudoku.lp instance.lp
 *      where instance.lp contains an encoding of a puzzle's initial state.
 *%

% Possible values range from 0..9
value(1..9).

% Each cell has a value assigned:
1 { sudoku(R, C, V) : value(V) } 1 :- value(R), value(C).

% Each row has exactly one assignment per value


% Each column has exactly one assignment per value

% Each 3x3 grid has exactly one assignment per value

% Show only solution predicates
#show sudoku/3.