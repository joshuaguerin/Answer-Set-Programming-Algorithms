%*
 * File: dominating_set.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a graph and an integer, n, find all dominating sets
 *              of size n.
 * Use: clingo dominating_set.lp instance.lp -c n=<val>
 *      where instance.lp contains node and edge predicates.
 *%

% Each node may be a member of the dominating set.
{dominating_set(X)} :- node(X).

% Define adjacency to a member of the dominating set.
set_adjacent(X) :- edge(X, Y), dominating_set(Y).
set_adjacent(Y) :- edge(X, Y), dominating_set(X).

% All nodes that aren't in the dominating set must be adjacent
% to a member of the dominating set.
:- node(X), not dominating_set(X), not set_adjacent(X).

% For a dominating set of size n:
% Dominating set must be of size n.
:- #count{X : dominating_set(X)} != n.

% For a minimal dominating set:
% Count the elements in the dominating set.
% count(C) :- C = #count{X : dominating_set(X)}.
% Minimize
% #minimize{C : count(C)}.

#show dominating_set/1.
