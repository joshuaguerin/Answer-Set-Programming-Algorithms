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
1 { sudoku(R, C, V) : value(C) } 1 :- value(R), value(V).

% Each column has exactly one assignment per value
1 { sudoku(R, C, V) : value(R) } 1 :- value(C), value(V).

% Each 3x3 grid has exactly one assignment per value
R=S :- sudoku(R, C, V), sudoku(S, D, V),
    (R-1)/3==(S-1)/3, (C-1)/3==(D-1)/3.

C=D :- sudoku(R, C, V), sudoku(S, D, V),
    (R-1)/3==(S-1)/3, (C-1)/3==(D-1)/3.

% Show only solution predicates
#show sudoku/3.