% File: max-sat.lp
% Author: Michael Huelsman
% Created On: 25 May 2026
% Purpose:
%   A CNF Max-SAT solver written in ASP.
%
% Usage:
%   clingo max-sat.lp instance.lp
%
% Instance Description:
%   Each instance contains the following predicates:
%     clause(C, L)
%       which reads that clause C contains literal L.
%   Literals are positive or negated integers.
%     E.g., (-1 v 3 v 4) would generate:
%       clause(C, -1). clause(C, 3). clause(C, 4).


% Extract literal information from clause() predicates. 
literal(L) :- L = |X|, clause(_, X).

% Extract clause information from clause() predcates.
clause(C) :- clause(C, _).

% A literal must have *exactly one* truth assignment. 
1 {true(L) ; false(L)} 1 :- literal(L).


% A clause is satisfied by any literal assignment:
%   (1) If a true-assigned literal appears positive, it is SAT.
sat_clause(C) :- clause(C, L), true(L), L > 0.

%   (2) If a false-assigned literal appears negated, it is SAT.
sat_clause(C) :- clause(C, L), false(|L|), L < 0.

% Maximize the number of satisfied clauses.
#maximize { 1, sat_clause(C) : sat_clause(C) }.

% Print truth assignment information, satisfied clauses.
#show true/1.
#show false/1.
#show sat_clause/1.
