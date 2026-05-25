% File: sat.lp
% Author: Michael Huelsman
% Created On: 25 May 2026
% Purpose:
%   A CNF 3-SAT solver written in ASP.
%
% Usage:
%   clingo 3-sat.lp instance.lp
%
% Instance Setup:
%   Each instance contains the following predicates:
%     clause(I,L1,L2,L3)
%       which reads that clause I contains literals L1, L2, and L3.
%   Literals values are only integers.
%   Negative integer values means a particular literal is negated in
%   the clause. Thus, clause(0, 1, 2, -3) is read as clause 0 is
%   x1 OR x2 OR (NOT x3).

% Simplification predicates
literal(X) :- X = |L|, clause(_,L,_,_).
literal(X) :- X = |L|, clause(_,_,L,_).
literal(X) :- X = |L|, clause(_,_,_,L).

clause(X) :- clause(X,_,_,_).

% Assign true/false values to literals
1 {true(X); false(X)} 1 :- literal(X).

% Clause satisfiability
sat_clause(X) :- clause(X,L,_,_,), true(L), L > 0.
sat_clause(X) :- clause(X,_,L,_,), true(L), L > 0.
sat_clause(X) :- clause(X,_,_,L,), true(L), L > 0.

sat_clause(X) :- clause(X,L,_,_,), false(|L|), L < 0.
sat_clause(X) :- clause(X,_,L,_,), false(|L|), L < 0.
sat_clause(X) :- clause(X,_,_,L,), false(|L|), L < 0.

% SAT constraints
:- not sat_clause(X), clause(X).
