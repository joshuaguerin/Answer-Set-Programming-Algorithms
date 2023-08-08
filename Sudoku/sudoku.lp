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
:- sudoku(R, C, V), sudoku(R, D, V), value(R), value(V), C!=D.

% Each column has exactly one assignment per value
:- sudoku(R, C, V), sudoku(S, C, V), value(C), value(V), R!=S.

% Each 3x3 grid has exactly one assignment per value

% Show only solution predicates
#show sudoku/3.