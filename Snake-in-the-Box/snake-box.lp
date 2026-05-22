#const n=3.

dim(n).
bits(0..N-1) :- dim(N).
node(0..(2**N - 1)) :- dim(N).
pow2(X) :- X = (2**N), node(X), bits(N).
largest_node((2**N)-1) :- dim(N).
adj(X,Y) :- node(X), node(Y), pow2(Z), Z=(X ^ Y), X < Y.
adj(Y,X) :- adj(X,Y).

1 {path(X,Y): adj(X,Y), node(X), node(Y)} N/2 :- N = 2**n.

path(X) :- path(X,_).
path(X) :- path(_,X).

1 {start(X): path(X)} 1.
1 {stop(X): path(X)} 1.

% Priming
path(0,1).
start(0).

% Cycle detection
% Reads node B is reachable on the path from node A.
path_reach(A,B) :- path(A,B).
path_reach(A,B) :- path_reach(A,C), path(C,B).

% Ensure no reverse edges
:- path(X,Y), path(Y,X).
% Ensure no branching
:- path(X,Y1), path(X,Y2), Y1 != Y2.
:- path(X1,Y), path(X2,Y), X1 != X2.
% Ensure continuity
:- path(X,Y), not path(_,X), not start(X).
:- path(X,Y), not path(Y,_), not stop(X).
% Ensure start and stop are connected to the path.
:- n > 1, path(X,Y), start(X), stop(Y).
:- start(X), not path(X,_).
:- stop(X), not path(_,X).
% No cycles
:- path_reach(X,X), path(X).
% No shortcuts
:- path(X), path(Y), adj(X,Y), not path(X,Y), not path(Y,X).


:~ N = {path(X,Y)}. [-N]


#show path/2.
% #show adjs/2.
% #show start/1.
% #show end/1.
