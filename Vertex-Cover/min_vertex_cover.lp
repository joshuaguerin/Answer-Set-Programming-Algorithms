%*
 * File: min_vertex_cover.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a graph and an integer, n, find all vertex covers
 *              of size n.
 * Use: clingo min_vertex_cover.lp instance.lp
 *      where instance.lp contains node and edge predicates.
 *%

% Each node may be a member of the vertex cover.
{cover(X)} :- node(X).

% Each edge must have at least one endpoint in the vertex cover.
1 {cover(X) ; cover(Y)} :- edge(X, Y).

% Count the elements in the vertex cover.
count(C) :- C = #count{X : cover(X)}.

% Minimize
#minimize{C : count(C)}.

#show cover/1.
