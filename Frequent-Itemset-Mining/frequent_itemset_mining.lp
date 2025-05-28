%*
 * File: frequent_itemset_mining.lp
 * Author: Joshua T. Guerin
 *
 * Description: Find patterns in items that are frequently co-located
 * 		together in transactions.
 * Use:
 *   clingo instance.lp frequent_itemset_mining.lp -c s=<support> -c n=<size>
 *
 *%

% Extract items from transaction data.
item(I) :- transaction(_, I).

% Items are candidates for each set.
{ set(I, S) : set(S) } :- item(I).

% Each nonempty itemset has an associated count of items.
count(S, C) :- set(S), C = #count{ I, S : set(I, S) }, C != 0.

% supports(T, S) - Transaction T supports itemset S.
% supports(T, S) :-	       

% Itemsets must have the correct count.
:- count(S, C), set(S), C != n.

#show count/2.
#show set/2.