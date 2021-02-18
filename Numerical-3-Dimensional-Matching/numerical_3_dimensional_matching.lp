%*
 * File: numerical_3_dimensional_matching.lp
 * Author: Joshua T. Guerin
 *
 * Description: Implementation of the Numerical 3 Dimensional Matching problem.
 * Use: clingo numerical_3_dimensional_matching.lp problem.lp -c n=<val>
 *      where problem.lp contains predicates enumerating x, y, and z.
 *%

% DEFINE
% Elements of a solution must come from x(), y(), and z().
{ solution(X, Y, Z) } :- x(X), y(Y), z(Z).

% Each element of X, Y, and Z must be in exactly one solution.
1 {solution(X, Y, Z) : y(Y), z(Z) } 1 :- x(X).
1 {solution(X, Y, Z) : x(X), z(Z) } 1 :- y(Y).
1 {solution(X, Y, Z) : x(X), y(Y) } 1 :- z(Z).

% TEST
% A solution must sum to the correct value.
:- solution(X, Y, Z), X+Y+Z != n.

% DISPLAY
#show solution/3.
