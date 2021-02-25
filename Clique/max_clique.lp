%*
 * File: max_clique.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a graph and an integer, n, find an n-clique in the graph.
 * Use: clingo clique.lp instance.lp
 *      where instance.lp contains node and edge predicates.
 *%

% Edges are undirected
edge(Y, X) :- edge(X, Y).

% All edges may be in the clique.
{clique(X, Y)} :- edge(X, Y).

% clique/1 lists individual nodes in the clique.
clique(X) :- clique(X, Y).
clique(Y) :- clique(X, Y).

% Any two vertices in the clique must be connected by an edge.
1 {clique(X, Y) ; clique(Y, X)} 1 :- clique(X), clique(Y), X != Y.

% Everything in the clique must have been an edge in the graph.
:- clique(X, Y), not edge(X, Y).

% For Max Clique
count(C) :- C = #count{X : clique(X)}.
#maximize{C : count(C)}.

% Display (either vertices or edges).
#show clique/1.
#show clique/2.
#show count/1.
