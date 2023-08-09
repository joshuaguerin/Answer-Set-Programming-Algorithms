%*
 * File: n_queens.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a graph and an integer, n, find an n-clique in the graph.
 * Use: clingo n_queens.lp -c n=size
 *      where size is the size of an nxn board.
 *%

values(1..n).

% queens(row, col).

% There are n queens placed.
n { queens(R, C) : values(R), values(C) } n.

% No two queens in the same row.
:- queens(R, C), queens(R, D), C!=D.

% No two queens in the same column.
:- queens(R, C), queens(S, C), R!=S.

% No two queens on the same diagonal.
:- queens(R, C), queens(S, D), R!=S, C!=D, R+C==S+D.
:- queens(R, C), queens(S, D), R!=S, C!=D, R-C==S-D.


#show queens/2.