%*
 * File: shortest_path.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a graph and an integer, n, find an n-clique in the graph.
 * Use: clingo shortest_path.lp instance.lp -c s=<val> -c e=<val>
 *%

start(s).
end(e).

% Edges are symmetric - an undirected graph.
% Directed representation is more concise.
edge(Y, X, C) :- edge(X, Y, C).

% Identify possible solution predicates.
{ path(X, Y, C) } :- edge(X, Y, C).

% Define reachability in the path.
reachable(S) :- start(S).
reachable(Y) :- reachable(X), path(X, Y, C).

% Ensure that there is a path from s to e.
:- end(E), not reachable(E).

% Mininmize the path length.
#minimize{C, X, Y : path(X, Y, C)}.

% Show solution predicate.
#show path/3.
