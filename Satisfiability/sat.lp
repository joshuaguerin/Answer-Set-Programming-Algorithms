% File: sat.lp
% Author: Michael Huelsman
% Created On: 25 May 2026
% Purpose:
%   A CNF SAT solver written in ASP.
%
% Usage:
%   clingo max-sat.lp instance.lp
%
% Instance Setup:
%   Each instance contains the following predicates:
%     clause(I,L)
%       which reads that clause I contains literal L.
%   Literals values are only integers.
%   Negative integer values means a particular literal is negated in
%   the clause. Thus, clause(0, -1) is read as clause 0 contains NOT x1.
%   Clauses may have any number of literals, but are assumed to be in CNF form.

% Simplification predicates

literal(L) :- L = |X|, clause(_,X).
clause(C) :- clause(C,_).

% Assign true/false values to literals
1 {true(L); false(L)} 1 :- literal(L).

% Clause satisfiability
sat_clause(C) :- clause(C,L), true(L), L > 0.
sat_clause(C) :- clause(C,L), false(|L|), L < 0.

% SAT constraints
:- not sat_clause(C), clause(C).
