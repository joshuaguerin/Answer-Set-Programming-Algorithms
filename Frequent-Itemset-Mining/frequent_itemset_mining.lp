%*
 * File: frequent_itemset_mining.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given an integer n, compute primes from 2..n
 * Use: clingo instance.lp frequent_itemset_mining.lp -c n=<min_support>
 *
 *%


item(I) :- transaction(_, I).

%count(C) :- C = #count{I : item(I)}.

transaction(C) :- C = #max{T : transaction(T, _)}.

% Create a graph from each transaction.
% I and J are associated with one another in transaction N.
associate(N, I, J) :- transaction(N, I), transaction(N, J), I!=J.

% Count occurrences of pairs with correct support
count(I, J, C) :- C = #count{ N : associate(N, I, J) }, n<=C,
	       	  item(I), item(J), I<J.

% Count occurrences of triplets with correct support
count(I, J, K, C) :- C = #count{ N : associate(N, I, J), associate(N, I, K) },
	       	     n<=C, item(I), item(J), item(K), I<J, J<K.

% Generalization needed

#show count/3.
#show count/4.
