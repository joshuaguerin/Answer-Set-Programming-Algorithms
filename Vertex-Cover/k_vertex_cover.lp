%*
 * File: k_vertex_cover.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a graph and an integer, n, find all vertex covers
 *              of size n.
 * Use: clingo k_vertex_cover.lp instance.lp -c n=<val>
 *      where instance.lp contains node and edge predicates.
 *%

% Each node may be a member of the vertex cover.
{cover(X)} :- node(X).

% Each edge must have at least one endpoint in the vertex cover.
1 {cover(X) ; cover(Y)} :- edge(X, Y).

% For a vertex cover of size n:
% The vertex cover must be of size n.
:- #count{X : cover(X)} != n.

#show cover/1.
