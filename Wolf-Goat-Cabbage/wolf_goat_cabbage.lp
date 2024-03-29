%*
 * File: wolf_goat_cabbage.lp
 * Author: Joshua T. Guerin
 *
 * Description: Implementation the Wolf/Goat/Cabbage boat puzzle.
 * Use: clingo instance.lp wolf_goat_cabbage.lp -c n=<val>
 *      where n is the number of steps allowed by the puzzle.
 *%

% Time is already discrete.
% We need some way to quantify time explicitly for grounding.
time(1..n).

% Note that x is only for empty (farmer-only) trips.
% It is an exception carved out for many of the rules below to simplify things.
at(x, l, T) :- time(T).
at(x, r, T) :- time(T).

% Each passenger is on exactly one side at any time.
1 { at(P, l, T) ; at(P, r, T) } 1 :- passenger(P), time(T), P!=x.

% The farmer may only be on one side at a time.
1 { at(f, l, T) ; at(f, r, T) } 1 :- time(T).

% If the farmer is on same side as a passenger they may enter the boat.
{ boat(P, T) } :- at(f, S, T), at(P, S, T), passenger(P).

% The boat moves a passenger at each timestep
at(P, r, T+1) :- boat(P, T), at(P, l, T), P!=x, T<n.
at(P, l, T+1) :- boat(P, T), at(P, r, T), P!=x, T<n.

% The boat moves the farmer
at(f, r, T+1) :- boat(_, T), at(f, l, T), T<n.
at(f, l, T+1) :- boat(_, T), at(f, r, T), T<n.

% Nothing else is moved by the boat.
at(P, S, T+1) :- passenger(P), not boat(P, T), at(P, S, T), P!=x, T<n.

% Enforce same-side rules:
% (1) Wolf will eat goat if unattended.
:- at(w, S, T), at(g, S, T), not at(f, S, T).

% (2) Goat eats cabbage if unattended.
:- at(g, S, T), at(c, S, T), not at(f, S, T).

% The boat only holds one passenger.
:- boat(P, T), boat(Q, T), P!=Q.

% Describe goal state: everyone is on the right.
at((f ; w ; g ; c), r, n).

#show at/3.
#show boat/2.

