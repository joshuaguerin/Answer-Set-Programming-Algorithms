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

% Color assignments must match arguments r, b
% I'm suddenly thinking this won't work until we define clique.
%:- #count{ X, Y : color(X, Y, red) } != r*2.
%:- #count{ X, Y : color(X, Y, blue) } != b*2.

%%%% Clique Constraints
% Note: Cliques will naturally exist as colors are assigned.

% Edge colors imply candidates for a clique.
% Vertices may (optionally) be in _either_ clique.
{ red(X) } :- color(X, Y, red).
{ red(Y) } :- color(X, Y, red).
{ blue(X) } :- color(X, Y, blue).
{ blue(Y) } :- color(X, Y, blue).

% Ensure that appropriate cardinality exists.
:- #count{ X : red(X) } != r.
:- #count{ X : blue(X) } != b.

% If two vertices are in a clique they must be
% connected by an appropraite edge.
%:- red(X), red(Y), not color(X, Y, red).
color(X, Y, red) :- red(X), red(Y), X != Y.
color(X, Y, blue) :- blue(X), blue(Y), X != Y.

% Identify cliques in the graph.
% 1 {clique(X, Y) ; clique(Y, X)} 1 :- clique(X), clique(Y), X != Y.



% Cardinalty: There must be a *red* clique of size r.
% red(C) :- C = #count{ X : clique(X, red) }.

% Cardinalty: There must be a *blue* clique of size b.
% blue(C) :- C = #count{ X : clique(X, blue) }.



%#show edge/2.
% #show clique/2.
%#show color/3.
%#show red/1.
%#show blue/1.
