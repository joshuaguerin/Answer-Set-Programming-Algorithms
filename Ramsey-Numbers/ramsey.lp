%*
 * File: ramsey.lp
 * Author: Joshua T. Guerin
 *
 * Description: Computes assignments based on the Ramsey therem:
 *              R(r, s) = k
 *              For a complete graph of k nodes, is there an assignment
 *              of 2 colors (red, blue) that have *either* a blue clique
 *              of size r *or* a red clique of size s.
 *
 * Use: clingo ramsey.lp -c k=<int> -c r=<int> -c s=<int>
 *      clingo ramsey.lp -c k=<int> -c r=<int> -c s=<int> -n 0
 *          where instance.lp contains node and edge predicates.
 *%

%%%% Elaborate the graph.

% There are k nodes in the graph.
node(1..k).

% The graph is complete: There are edges between all pairs.
edge(X, Y) :- node(X), node(Y), X < Y.

%%%% Coloring requirements are met.

% Set of available colors.
color(red ; blue).

% All nodes are assigned exactly one color.
1 { color(X, C) : color(C) } 1 :- node(X).

%%%% Ensure the clique is there.

% All edges are candidates for the clique.
% Colors derived from the color assignment.
{ clique(X, C) } :- color(X, C).

% Cardinalty: There must be a *blue* clique of size r.
:- #count{ X : clique(X, blue) } != r.

% Cardinalty: There must be a *red* clique of size s.
:- #count{ X : clique(X, red) } != s.

#show edge/2.
#show clique/2.