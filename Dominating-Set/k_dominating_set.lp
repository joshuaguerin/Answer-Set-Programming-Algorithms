%*
 * File: k_dominating_set.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a graph and an integer, n, find all dominating sets
 *              of size n.
 * Use: clingo dominating_set.lp instance.lp -c n=<val>
 *      where instance.lp contains node and edge predicates.
 *%

% Each node may be a member of the dominating set.
{set(X)} :- node(X).

% Define adjacency to a member of the dominating set.
set_adjacent(X) :- edge(X, Y), set(Y).
set_adjacent(Y) :- edge(X, Y), set(X).

% All nodes that aren't in the dominating set must be adjacent
% to a member of the dominating set.
:- node(X), not set(X), not set_adjacent(X).

% Dominating set must be of size n.
:- #count{X : set(X)} != n.

#show set/1.
