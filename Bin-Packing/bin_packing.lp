%*
 * File: bin_packing.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a set of (value, weight) pairs, and parameter n,
 *              select the maximize the value of included items while
 *              not exceeding a weight of n.
 * Use: clingo bin_packing.lp instance.lp -c n=<val>
 *      where instance.lp contains item predicates.
 *%

% The number of possible bins is equal to the possible items.
% Each item may be included in any bin.
{ bin(B, N) } :- item(B), item(N).

% Each item must be included in exactly one bin.
1 { bin(B, N) : item(B) } 1 :- item(N).

% Create a set of bins in the solution.
bin(B) :- bin(B, N).

% Compute how much is stored in each bin.
weight(B, T) :- T = #sum{C : bin(B, I), item(I, C)}, bin(B).

% Bins can pack items with a max cost of n.
:- bin(B), weight(B, W), n < W.

% More sensible numbering (rather than arbitrary bin numbers).
%#minimize{B : bin(B)}.

% Count the total number of bins
count(C) :- C = #count{B : bin(B)}.

#minimize{C : count(C)}.

#show bin/2.
#show weight/2.
