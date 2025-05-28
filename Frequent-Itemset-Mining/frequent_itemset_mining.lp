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

% Extract a list of transactions.
transaction(T) :- transaction(T, _).

% Extract items from transaction data.
item(I) :- transaction(_, I).

% Items are candidates for each set.
{ set(I, S) : set(S) } :- item(I).

% Each nonempty itemset has an associated count of items.
count(S, C) :- set(S), C = #count{ I : set(I, S) }, C != 0.

% supports(T, S) - Transaction T supports itemset S.
%supports(T, S) :- s { set(I, S) : transaction(T, I) } s.

% Supporting transactions are supersets of item sets.
support(T, S, I) :- set(I, S), transaction(T, I).

% support(S, C) set(S) has support count C

support(S, C) :- C = #count{ I : support(T, S, I) },
                     set(S), transaction(T), C != 0.


% Itemsets must have the correct count.
:- count(S, C), set(S), C != n.

#show count/2.
#show set/2.
#show support/2.
#show support/3.
