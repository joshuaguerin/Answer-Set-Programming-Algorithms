%*
 * File: equal_sum_partition.lp
 * Author: Joshua T. Guerin
 *
 * Description: Partition a set of values into two sets with equal sum.
 * Use: clingo equal_sum_partition.lp instance.lp
 *      where instance.lp contains a predicate defining values.
 *%

% Each value must be a member of a or b.
1 {a(V) ; b(V)} 1 :- value(V).

% Compute sums for sets a and b.
total(a, S) :- S = #sum{A : a(A)}.
total(b, S) :- S = #sum{B : b(B)}.

% Sets a and b must have the same sum.
:- total(a, S), total(b, S'), S != S'.


#show a/1.
#show b/1.
#show total/2.
