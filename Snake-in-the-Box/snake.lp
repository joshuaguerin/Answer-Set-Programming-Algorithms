
%% Instance

% The total number of bits, as individual labels.
% Enough has changed that I'm not 100% certain this phase is necessary.
bits(a, b, c).

bit(A) :- bits(A, B, C).
bit(B) :- bits(A, B, C).
bit(C) :- bits(A, B, C).

% Generate all possible vertices.
vertex(T, U, V) :- bits(A, B, C), value(T), value(U), value(V).

% Assignments are binary.
value(0 ; 1).

% Define adjacency
adjacent((T, U, V) , (W, X, Y)) :- vertex(T, U, V), vertex(W, X, Y),
																	 T < W, U == X, V == Y.
adjacent((T, U, V) , (W, X, Y)) :- vertex(T, U, V), vertex(W, X, Y),
																	 T == W, U < X, V == Y.
adjacent((T, U, V) , (W, X, Y)) :- vertex(T, U ,V), vertex(W, X, Y),
																	 T == W, U =  X, V < Y.

%% Defining Paths

% Define an eventual starting, ending point.
{ first(X, Y, Z) } :- vertex(X, Y, Z).
 {  last(X, Y, Z) } :- vertex(X, Y, Z).

% Exactly one first/last assignment.
:- #count{ X, Y, Z : first(X, Y, Z) } != 1.
:- #count{ X, Y, Z :  last(X, Y, Z) } != 1.

% The start and aren not the same assignment
:- first(T, U, V), last(X, Y, Z), T != X, U != Y, V != Z.

% Every Pair is a candidate for the path.
{ path((T, U, V) , (W, X, Y)) } :- adjacent((T, U, V) , (W, X, Y)).

% Define reachabilty.

% Define path.

% Define additional problem parameters (e.g., adjacency).

% Locate the longest such path.
% #maximize

% Display
% #show pred/arity.
