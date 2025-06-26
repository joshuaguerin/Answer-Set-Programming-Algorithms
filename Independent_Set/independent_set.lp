%*
 * File: set.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a graph, find the maximal independent
 *              set of the graph.
 * Use: clingo independent_set.lp instance.lp
 *%

% Each node may be a member of the independent set.
{set(X)} :- node(X).

% No two adjacent vertices are in the independent set.
:- edge(X, Y), set(X), set(Y).

% Count the elements in the independent set.
count(C) :- C = #count{X : set(X)}.

% Minimize the size of the independent set.
#maximize{C : count(C)}.

#show set/1.
