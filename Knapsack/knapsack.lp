%*
 * File: knapsack.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a set of (value, weight) pairs, and parameter n,
 *              select the maximize the value of included items while
 *              not exceeding a weight of n.
 * Use: clingo knapsack.lp instance.lp -c n=<val>
 *      where instance.lp contains item predicates.
 *%

% Every item may be in the knapsack.
{knapsack(V, W)} :- item(V, W).

% Compute total weight, value, and count of items.
weight(S) :- S = #sum{W, V : knapsack(V, W)}.
value(S) :- S = #sum{V, W : knapsack(V, W)}.
count(C) :- C = #count{V, W : knapsack(V, W)}.

% Total weight may not exceed n.
:- weight(W), W>n.

% Maximize individual values.
#maximize{V, W : value(V), weight(W)}.

#show knapsack/2.
#show weight/1.
#show value/1.
#show count/1.
