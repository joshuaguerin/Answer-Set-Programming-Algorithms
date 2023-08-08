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

boundary(1, 3).
boundary(4, 6).
boundary(7, 9).

% Each cell has a value assigned:
1 { sudoku(R, C, V) : value(V) } 1 :- value(R), value(C).

% Each row has exactly one assignment per value
1 { sudoku(R, C, V) : value(C) } 1 :- value(R), value(V).

% Each column has exactly one assignment per value
1 { sudoku(R, C, V) : value(R) } 1 :- value(C), value(V).

% Each 3x3 grid has exactly one assignment per value

% Simplest abstraction: These two cells cannot have the same value
%:- sudoku(1, 2, V), sudoku(2, 3, V).

% Next abstraction: specific grids
% grid 1 cannot have a repeat
R=S :- sudoku(R, C, V), sudoku(S, D, V), R=1..3, C=1..3, S=1..3, D=1..3.
C=D :- sudoku(R, C, V), sudoku(S, D, V), R=1..3, C=1..3, S=1..3, D=1..3.

% grid 2 cannot have a repeat
R=S :- sudoku(R, C, V), sudoku(S, D, V), R=1..3, C=4..6, S=1..3, D=4..6.
C=D :- sudoku(R, C, V), sudoku(S, D, V), R=1..3, C=4..6, S=1..3, D=4..6.

% Each element can only occur once per grid.
R=S :- sudoku(R, C, V), sudoku(S, D, V), boundary(B1, B2), boundary(B3, B4),
    R=B1..B2, C=B3..B3, S=B1..B2, D=B3..B4.

C=D :- sudoku(R, C, V), sudoku(S, D, V), boundary(B1, B2), boundary(B3, B4),
    R=B1..B2, C=B3..B3, S=B1..B2, D=B3..B4.

% Show only solution predicates
#show sudoku/3.