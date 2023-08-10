%*
 * File: hamiltonian_path.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a graph and an integer, n, find an n-clique in the graph.
 * Use: clingo hamiltonian_path.lp instance.lp -c s=<val> -c e=<val>
 *%

start(s).
end(e).

% Edges are symmetric - an undirected graph.
% Directed representation is more concise.
edge(Y, X, C) :- edge(X, Y, C).

% Identify possible solution predicates.
{ path(X, Y, C) } :- edge(X, Y, C).

% Each node has a maximum of one incoming, outgoing edge.
{ path(X, Y, C) : edge(X, Y, C) } 1 :- node(Y).
{ path(X, Y, C) : edge(X, Y, C) } 1 :- node(X).

% Start may not have an incoming edge, end cannot have an outgoing edge.
:- start(S), path(X, S, C).
:- end(E), path(E, Y, C).

% Define reachability in the path.
reachable(S) :- start(S).
reachable(Y) :- reachable(X), path(X, Y, C).

% Ensure that there is a path from s to e.
:- end(E), not reachable(E).

% All nodes must be reachable from the start (Hamiltonian property).
:- node(X), not reachable(X).

% Show solution predicate.
#show path/3.
