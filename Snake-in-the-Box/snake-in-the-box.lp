%*
 * File: snake_in_the_box.lp
 * Author: Michael Huelsman
 *
 * Description: Given a positive integer n, find a longest snake for a
 *  n-dimensional hypercube graph.
 *
 * Use: clingo snake_in_the_box.lp -c n=dimension
 *      where dimension is the dimension of the hypercube.
 *%

% Define hypercube vertices.
dim(n). % Here for easier output.
bits(0..n-1).
vertex(0..(2**n - 1)).
% Define the edges in the hypercube graph.
pow2(X) :- X = (2**N), N = 0..n.
edge(X,Y) :- vertex(X), vertex(Y), pow2(Z), Z=(X ^ Y), X < Y.
edge(Y,X) :- edge(X,Y).


% Select a number of edges in the hypercube to be part of the path.
% We know there must be at least n-1 edges, and no more than 2^(n-1).
(n-1) {path(X,Y): edge(X,Y), vertex(X), vertex(Y)} 2**(n-1).

% Define which vertices are on the path.
path(X) :- path(X,_).
path(X) :- path(_,X).

% There can only be one start vertex and one stop vertex in the path.
1 {start(X): path(X)} 1.
1 {stop(X): path(X)} 1.

% Prime the path by giving it an initial sequence start.
% Since the starting point and edge is arbitrary we choose the edge from 0 -> 1.
path(0,1).
start(0).

% Reachability predicate which we use for cyclic path detection.
% Reads vertex B is reachable on the path from vertex A.
path_reachable(A,B) :- path(A,B).
path_reachable(A,B) :- path_reachable(A,C), path(C,B).

% Ensure no reverse edges.
:- path(X,Y), path(Y,X).
% Ensure no branching paths.
:- path(X,Y1), path(X,Y2), Y1 != Y2.
:- path(X1,Y), path(X2,Y), X1 != X2.
% Ensure continuity (only for n > 2).
:- n > 2, path(X,Y), not path(_,X), not start(X).
:- n > 2, path(X,Y), not path(Y,_), not stop(X).
% Ensure start and stop are connected to the path.
:- n > 1, path(X,Y), start(X), stop(Y). % Only if there is > 1 possible path.
:- start(X), not path(X,_).
:- stop(X), not path(_,X).
% The path cannot contain a cycle.
:- path_reachable(X,X), path(X).
% Two (non-consecutive) vertices on the path share an edge in the hypercube.
:- path(X), path(Y), edge(X,Y), not path(X,Y), not path(Y,X).

% Maximize the number of edges in the path.
#maximize { 1,path(X,Y): path(X,Y) }.

% Only display the edges on the path.
#show path/2.
#show dim/1.
