%*
 * File: ramsey.lp
 * Author: Joshua T. Guerin
 *
 * Description: Computes assignments based on the Ramsey theorem:
 *              R(r, b) = k
 *              For a complete graph of k nodes, is there an assignment
 *              of 2 colors (red, blue) that have *either* a red clique
 *              of size r *or* a blue clique of size b
 *
 *              We are searching for an assignment that lacks either.
 *
 * Use: clingo search.lp -c k=<int> -c r=<int> -c b=<int>
 *      clingo search.lp -c k=<int> -c r=<int> -c b=<int> -n 0
 *          where instance.lp contains node and edge predicates.
 *%

%%%% Elaborate the graph.

% There are k nodes in the graph.
node(1..k).

% The graph is complete: There are edges between all pairs.
% The edges are undirected: edge(X, Y) and edge(Y, X).
edge(X, Y) :- node(X), node(Y), X != Y.


%%%% Coloring requirements are met.

% Set of available colors.
color(red ; blue).

% All _edges_ are assigned exactly one color.
1 { color(X, Y, C) : color(C) } 1 :- edge(X, Y).

% ^Sub-constraint: Consider edge symmetry for color assignment.
color(Y, X, C) :- color(X, Y, C).


%%%% Clique Constraints

% Edge colors imply candidates for a clique.
% Up to r/b vertices may (optionally) be in red/blue cliques.
{ red(X) } r :- color(X, Y, red).
{ red(Y) } r :- color(X, Y, red).
{ blue(X) } b :- color(X, Y, blue).
{ blue(Y) } b :- color(X, Y, blue).

% If two vertices are in a clique they must be
% connected by an appropraite edge.
color(X, Y, red) :- red(X), red(Y), X != Y.
color(X, Y, blue) :- blue(X), blue(Y), X != Y.

% Need one of the two cliques to exist.
result(success) :- #count{ X : red(X) } == r.
result(success) :- #count{ X : blue(X) } == b.

% Weed out incorrect color assignments:
% May only have r, b, or 0 nodes of a particular color.
:- #count{ X : red(X) } != r, #count{ X : red(X) } != 0.
:- #count{ X : blue(X) } != b, #count{ X : blue(X) } != 0.

% At least one of the cliques must exist.
:- not result(success).
